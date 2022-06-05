import pyforest
from pyforest import LazyImport

# HuggingFace
datasets = LazyImport("import datasets")
load_metric = LazyImport("from datasets import load_metric")
load_dataset = LazyImport("from datasets import load_dataset")
Dataset = LazyImport("from datasets import Dataset")
DatasetDict = LazyImport("from datasets import DatasetDict")


transformers = LazyImport("import transformers")
Trainer = LazyImport("from transformers import Trainer")
TrainingArguments = LazyImport("from transformers import TrainingArguments")
AutoTokenizer = LazyImport("from transformers import AutoTokenizer")
AutoConfig = LazyImport("from transformers import AutoConfig")
AutoModel = LazyImport("from transformers import AutoModel")
AutoModelForSequenceClassification = LazyImport("from transformers import AutoModelForSequenceClassification")
AutoModelForTokenClassification = LazyImport("from transformers import AutoModelForTokenClassification")
AutoModelForMultipleChoice = LazyImport("from transformers import AutoModelForMultipleChoice")
AutoModelForQuestionAnswering = LazyImport("from transformers import AutoModelForQuestionAnswering")
AutoModelForMaskedLM = LazyImport("from transformers import AutoModelForMaskedLM ")

# Helpers
ftfy = LazyImport("import ftfy")
fc = LazyImport("import funcy as fc")
warnings = LazyImport("import warnings")
random = LazyImport("import random")
itertools = LazyImport("import itertools")
appdirs = LazyImport("import appdirs")
copy = LazyImport("import copy")
defaultdict = LazyImport("from collections import defaultdict")
Counter = LazyImport("from collections import Counter")
edict = LazyImport("from easydict import EasyDict as edict")
Xp = LazyImport("from xpflow import Xp")
millify = LazyImport("from millify import millify")

wandb = LazyImport("import wandb")
StringIO = LazyImport("from io import StringIO")
dataclass =  LazyImport("dataclasses import dataclass")
requests = LazyImport("import requests")
string = LazyImport("string")
time = LazyImport("time")
exrex = LazyImport("exrex")
