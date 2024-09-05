# Copyright (C) 2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import json
import logging
import os
import random

import tokenresponse as token

cwd = os.path.dirname(__file__)
filename = f"{cwd}/../dataset/finrag.json"
qlist = []
try:
    with open(filename) as qfile:
        qlist = json.load(qfile)
except:
    logging.error(f"Question File open failed: {filename}")
    exit()


def getUrl():
    return "/v1/finqna"


def getReqData():
    qlen = len(qlist)
    qid = random.randint(0, qlen - 1)
    logging.debug(f"Selected question: {qlist[qid]['question']}")

    return {"messages": qlist[qid]["question"], "max_tokens": 128}


def respStatics(environment, reqData, respData):
    return token.respStatics(environment, reqData, respData)


def staticsOutput(environment, reqlist):
    token.staticsOutput(environment, reqlist)
