/*
Iasmin e Maria Luiza foram contratadas para criar um sistema de gestão de RH, necessitando criar as tabelas a
seguir e, posteriormente realizar as consultas listadas as seguir:
Funcionarios (Matricula, PrimeiroNome,SegundoNome, UltimoNome, CPF, RG, Endereco, CEP,Cidade, Fone,
Funcao, Salario)
Departamentos (Codigo, Nome, Localizacao, NomeGerente)
Consultas a serem criadas:
• Listar nome e sobrenome dos funcionários ordenado por sobrenome
• Listar todos os campos de funcionários ordenados por cidade
• Liste os funcionários que têm salário superior a R$ 1.000,
• Liste o primeiro nome dos funcionários
• Liste o total da folha de pagamento (usando sum)
• Liste a quantidade de funcionários desta empresa (usando count)
*/

create table funcionarios (
	matricula int auto_increment,
    nome varchar(20),
    sobrenome varchar(20), 
    cidade varchar(30),
    salario float,
    primary key(matricula)
);

insert into funcionarios (nome,sobrenome,cidade,salario)
values("alison", "Barbosa","campina grande",100000);

insert into funcionarios (nome,sobrenome,cidade,salario)
values("gabriel", "Barbosa","minas gerais",10000);

insert into funcionarios (nome,sobrenome,cidade,salario)
values("renan", "pereira","joão pessoa",800);

select nome,sobrenome from funcionarios order by sobrenome; 
select * from funcionarios order by cidade;
select *  from funcionarios where salario > 1000;
select nome from funcionarios;
select sum(salario) from funcionarios;
select count(*) from funcionarios;