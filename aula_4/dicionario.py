meuDicionario = {
    "nome"     : "Wesley", 
    "sobrenome": "Ribeiro",
    'anos'     : 37
    };

print(meuDicionario);

frutaDicionario = { 
    'maçã'   : 3,
    'banana' : 6,
    'uva'    : 8,
};

print("Significado encontrado no dicionário : ", frutaDicionario["maçã"]);
print();

frutaDicionario["maçã"] = 5;
frutaDicionario["laranja"] = 10;

print("Nova quantidade de maçã: ", frutaDicionario["maçã"]);
print();
print(frutaDicionario);

print(frutaDicionario);
print();

animaisDicionario = {};
animaisDicionario["cachorro"] = "Melissa";
print(animaisDicionario);
print();

aluno = {
    'nome'     : 'Wesley', 
    'anos'     : 37 ,
    'hobbies'  : ['jogar', 'esportes']
    };

print(aluno);
print();

frutaDicionario = { 
    'maçã'   : 3,
    'banana' : 6,
    'uva'    : 8,
    'vitaminas' : {'a' : 'boa pra ele'}
};

print(frutaDicionario["vitaminas"]["a"]);