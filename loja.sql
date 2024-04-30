create database loja;
use loja;

create table produtos(
id int not null primary key,
nome varchar(50) not null,
preco float not null
);

insert into produtos(id, nome, preco) values(1, 'leite integraal', 6.90);
select *from produtos;

alter table produtos modify id varchar(15);
alter table produtos add imagem varchar(100);

update produtos set imagem = 'https://acesse.dev/85RKt' where id ="1";

update produtos set id="LT01" where id="1";

select *from produtos