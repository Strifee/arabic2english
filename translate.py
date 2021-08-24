from data_processing import SRC, TRG, engTokenizer
import torch
import device
from train import model

def translate_sentence(model,sentence,srcField,targetField,srcTokenizer):
    model.eval()
    processed_sentence = srcField.process([srcTokenizer(sentence)]).to(device)
    trg = ["بداية"]

    for _ in range(60):
        trg_indecies = [targetField.vocab.stoi[word] for word in trg]
        trg_tensor = torch.LongTensor(trg_indecies).unsqueeze(1).to(device)
        outputs = model(processed_sentence,trg_tensor)
        
        if targetField.vocab.itos[outputs.argmax(2)[-1:].item()] == "<unk>":
            continue 
        trg.append(targetField.vocab.itos[outputs.argmax(2)[-1:].item()])
        if targetField.vocab.itos[outputs.argmax(2)[-1:].item()] == "نهاية":
            break
    return " ".join([word for word in trg if word != "<unk>"][1:-1])


if __name__ == '__main__':
        print("I'm home -> {}",translate_sentence(model,"I'm at home" ,SRC,TRG,engTokenizer))
        print("I'm alone -> {}",translate_sentence(model,"I'm alone" ,SRC,TRG,engTokenizer))