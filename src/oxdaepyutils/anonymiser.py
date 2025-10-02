#!/usr/bin/env python3

#  Copyright 2024-2025 Oxford PSI DAE Python Utils Collaborators
#  SPDX-License-Identifier: Apache-2.0

import random
import string
import csv
import pandas as pd
import os.path

class Anonymiser:
    def __init__(self,linkFile):
        self.linkFile = linkFile
        self.linksMap = {}
        self.maxLength = 6
        self._readFile()

    def _readFile(self):
        # Load link file (if it exists). Don't fail if it doesn't exist.
        if os.path.isfile(self.linkFile):
            self.linksMap = {}
            
            with open(self.linkFile,'r') as f:
                for row in csv.reader(f, lineterminator='\n', delimiter=','):
                    # print(f"row: {row}")
                    if None != row and len(row) > 0:
                        self.linksMap[row[0]] = row[1]


    def getMaxLength(self):
        return self.maxLength

    def size(self):
        return len(self.linksMap)

    def persist(self):
        with open(self.linkFile,'w') as f:
            w = csv.writer(f, lineterminator='\n', delimiter=',')
            # w.writerow("key,value")
            w.writerows(self.linksMap.items())
        return True

    def anonymise(self,valueListOrSeries): # TODO specify 3 types supported
        if isinstance(valueListOrSeries,str):
            return self._anonymiseSingle(valueListOrSeries)
        if isinstance(valueListOrSeries, list):
            result = []
            for value in valueListOrSeries:
                result.append(self._anonymiseSingle(value))
            return result
        if isinstance(valueListOrSeries, pd.Series):
            result = valueListOrSeries.copy()
            for index,value in valueListOrSeries.items():
                result.loc[index] = self._anonymiseSingle(value)
            # s = pd.Series(result)
            # s.reindex(valueListOrSeries.index)
            return result

        raise TypeError(f"Type for valueListOrSeries not supported: '{type(valueListOrSeries)}'")

    def _anonymiseSingle(self,singleValue):
        if singleValue not in self.linksMap:
            self.linksMap[singleValue] = self._genValue()
        return self.linksMap[singleValue]

    def _genValue(self):
        # TODO consider only using values that are hard to mistake for each other (I.e. not 1, I, etc.)
        newValue = ''
        # Ensure we don't accidentally generate a duplicate key
        while newValue == '' or newValue in self.linksMap:
            newValue = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(self.maxLength))
        return newValue