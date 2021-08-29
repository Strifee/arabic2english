
# Arabic2English - Arabic to English Translator

**This is a PyTorch implementation of an Arabic to English Neural Machine Translation built using Transformers architecture ([Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf))**


# Setup and Requirements
**1. CUDA:**
<br/>
install [CUDA](https://developer.nvidia.com/cuda-downloads) before installing the required packages or check if it is already installed 
<br/>
<br/>
**2. Clone the Translate repo:**
```
$ git clone clone https://github.com/Strifee/arabic2english.git
```
**3. install requirements:**
```
pip install -r requirements.txt
```
`if you have problem with CUDA package try this:`
```
conda install -q pytorch torchvision cudatoolkit=11 -c pytorch-nightly
```

# Data
**1. Arab-Acquis Dataset :**

[Arab-Acquis](https://aclanthology.org/E17-2038.pdf) is a large dataset for evaluating machine translation between 22 European languages and Arabic. Arab-Acquis consists of over 12,000 sentences from the JRCAcquis (Acquis Communautaire) corpus translated twice by professional translators, once from English and once from French, and totaling over 600,000 words. 
<br/>

`Download Arab-Acquis dataset and put it into folder `

<br/>

**2. Arabic to English Translation Sentences :**

[Arabic to English Translation Sentences](https://www.kaggle.com/samirmoustafa/arabic-to-english-translation-sentences) is a dataset for machine translation between English  and Arabic.

# Training

**1. Clone the Translate repo:**
```
$ git clone clone https://github.com/Strifee/arabic2english.git
```
**2. Training**
```
$ python translate.py
```
# Results

# Example

```
$ git clone clone https://github.com/Strifee/arabic2english.git
```
