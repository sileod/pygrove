# pygrove

Writing the same imports over and over is draining. Some imports are standard enough for automation.  [pyforest](https://github.com/8080labs/pyforest) allows this, but it is not frequently updated and oriented towards general data science.
Here, I provide other imports, including some huggingface libraries imports.

# Installation
`pip install pygrove`

# Usage
```python
import pygrove
model = AutoModel.from_pretrained('roberta-base')
tokenizer = AutoTokenizer.from_pretrained('roberta-base') 
```
Please note that thanks to pyforest, pygrove imports are lazy. Objects do not require time or memory until they are actually called.

# Imports

Here is the list of pygrove imports
```python
# HuggingFace
datasets = LazyImport("import datasets")
load_metric = LazyImport("from datasets import load_metric")
load_dataset = LazyImport("from datasets import load_dataset")
Dataset = LazyImport("from datasets import Dataset")

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

# Helpers
ftfy = LazyImport("import ftfy")
fc = LazyImport("import funcy as fc")
warnings = LazyImport("import warnings")
tqdm = LazyImport("from tqdm.auto import tqdm")
random = LazyImport("import random")
itertools = LazyImport("import itertools")
appdirs = LazyImport("import appdirs")
copy = LazyImport("import copy")
defaultdict = LazyImport("from collections import defaultdict")
Counter = LazyImport("from collections import Counter")
edict = LazyImport("from easydict import EasyDict as edict")
Xp = LazyImport("from xpflow import Xp")
millify = LazyImport("from millify import millify")
```
