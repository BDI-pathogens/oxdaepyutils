#!/usr/bin/env python3

#  Copyright 2024-2025 Oxford PSI DAE Python Utils Collaborators
#  SPDX-License-Identifier: Apache-2.0

# Test the anonymiser class

import sys
sys.path.append("..")

import os.path

from oxdaepyutils.anonymiser import Anonymiser as Anon

import pandas as pd

from numpy.testing import (assert_equal)


def test_empty():
    an = Anon("./output/dummy-anon.csv")
    assert_equal(an.size(),0)

def test_single():
    # delete file if it exists
    fname = "./output/dummy-anon2.csv"
    if os.path.isfile(fname):
        os.remove(fname)

    an = Anon(fname)
    assert_equal(an.size(),0) # kept here incase deletion fails
    # Add a single entry
    res = an.anonymise("someValue")
    assert(res is not None) #"Should return a value")
    assert(len(res) > 0) #"Should be a non empty value")

    # Verify length is the same as the class maxLength value
    assert_equal(len(res),an.getMaxLength(),"Value length should equal class maxLength property")

    assert_equal(an.size(),1)
    assert(an.persist())
    # check file exists
    assert(os.path.isfile(fname)) #"Output map file should exist")
    # delete file
    os.remove(fname)


def test_duplicate():
    an = Anon("./output/dummy-anon3.csv")
    
    # Add a single entry
    res = an.anonymise("someValue")
    assert_equal(an.size(),1)
    assert(res is not None)
    assert(len(res) > 0)
    
    # Add the same entry
    res2 = an.anonymise("someValue")
    assert_equal(an.size(),1)

    assert_equal(res,res2)

def test_list():
    an = Anon("./output/dummy-anon4.csv")
    mylist = ["first","second","third","third","fourth"]
    res = an.anonymise(mylist)
    assert(res is not None)
    assert_equal(len(res), 5, "Anonymise call should return same number of values as passed to it")
    uniqueSet = set(res)
    assert_equal(len(uniqueSet),4,"Unique results should have 4 values")

def test_series():
    an = Anon("./output/dummy-anon5.csv")
    mylist = ["first","second","third","third","fourth"]
    myseries = pd.Series(mylist)
    res = an.anonymise(myseries)
    assert(res is not None)
    assert(isinstance(res,pd.Series))
    print("res in order:-")
    print(res)
    # Check that the two 'third' values have the same anonymised value
    assert_equal(res.loc[2],res.loc[3],"Both 'third' values should be the same")

    # Now reorder the original Series, and try again
    myseries = myseries.sort_values(ascending=True)
    res2 = an.anonymise(myseries)
    print("res2 in order:-")
    print(res2)
    # Now try the reordered values
    assert_equal(res2.loc[2],res.loc[3],"Reordered values should be the same")

def test_persistance():
    # delete file if it exists
    fname = "./output/dummy-anon6.csv"
    if os.path.isfile(fname):
        os.remove(fname)

    an = Anon(fname)
    mylist = ["first","second","third","third","fourth"]
    res = an.anonymise(mylist)
    assert(an.persist())

    # Now load persistence, apply a second time, and check results are equal
    an2 = Anon(fname)
    res2 = an2.anonymise(mylist)
    assert_equal(res2,res,"Result lists should match")

    # delete file
    os.remove(fname)

# TODO Consider adding a test of unique values (i.e. key unique count and value unique count are the same)
# Note: May need to reduce the character count on maxLength to make collisions more likely (at the cost of time)