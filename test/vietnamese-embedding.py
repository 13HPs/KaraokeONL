from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s
model = SentenceTransformer("dangvantuan/vietnamese-embedding")

sentences = [
    "SƠN TÙNG M-TP",
    "Jack97",
]
tokenizer11 = [tokenize(remove_accents(sent).lower()) for sent in sentences]
tokenizer12 = [tokenize(sent.lower()) for sent in sentences]
# tokenizer_sent = [tokenize(sent.lower()) for sent in sentences]
print('tokenizer11', tokenizer11)

embedding11 = model.encode(tokenizer11)
embedding12 = model.encode(tokenizer12)
sentences2 = [
    "j97",
    "sổn tũng ptm",
    "mtp",
    "jack",
    "sơn tùng mtp"
]
tokenizer21 = [tokenize(remove_accents(sent).lower()) for sent in sentences2]
tokenizer22 = [tokenize(sent.lower()) for sent in sentences2]
# tokenizer_sent2 = [tokenize(sent.lower()) for sent in sentences2]

embeddings21 = model.encode(tokenizer21)
embeddings22 = model.encode(tokenizer22)

similarities = model.similarity(embedding11, embeddings21)
similarities2 = model.similarity(embedding12, embeddings22)
print(similarities)
print(similarities2)
print(similarities2+similarities)


