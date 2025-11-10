
# atvidade_sql1

CREATE TABLE → criar tabelas

INSERT INTO → inserir registros

SELECT → consultar registros

UPDATE → atualizar informações

DELETE → remover dados

ALTER TABLE → modificar estrutura

DROP TABLE → excluir tabela

# Divisão do exercício

python criar_tabela_livros.py
python consultar_disponiveis.py
python atualizar_disponibilidade.py
python ordenar_por_ano.py
python criar_tabela_usuario.py
python alterar_tabela_usuario.py
python apagar_tabela_usuario.py



1 - Por que os bancos de dados são essenciais em aplicações modernas?

Os bancos de dados permitem armazenar e organizar grandes volumes de informações, facilitando o acesso e a análise dos dados. Eles auxiliam na tomada de decisões estratégicas, aumentando a produtividade e automatizando tarefas. Também contribuem para melhorar o relacionamento com clientes, oferecendo um atendimento mais personalizado. Além disso, são essenciais na gestão de recursos humanos e no controle de estoques e logística, otimizando processos e recursos das empresas.

https://blog.dsacademy.com.br/

2 - Quais são as duas principais categorias de bancos de dados

 Bancos de dados relacionais e não relacionais

 https://aws.amazon.com/pt/compare/the-difference-between-relational-and-non-relational-databases/


3 - Em quais cenários é recomendado utilizar um banco de dados
relacional? (Descreva situações ideais para SQL)

Pense no banco de dados relacional como uma coleção de arquivos de planilha que ajuda empresas a organizar, gerenciar e relacionar dados. No modelo de banco de dados relacional, cada "planilha" é uma tabela que armazena informações, representadas por colunas (atributos) e linhas (registros ou tuplas). 

https://cloud.google.com/learn/what-is-a-relational-database?hl=pt-BR

4 - De que forma os recursos de hardware (CPU, memória, disco) afetam a
performance de um banco de dados? 

o banco de dados deve ficar em um servidor exclusivo para isso. Isso porque banco de dados demandam um tempo de resposta muito rápido. Se os processos do sistema operacional estiverem sendo divididos para tratar outros tipos de requisições, como gerenciamento de domínio, servidor de arquivos, ou qualquer outro processo, isso pode impactar significativamente a performance do banco de dados.

https://www.ajuda.vinhasoft.com.br/base-conhecimento/performance-do-banco-de-dados/


5 - O que significa escalabilidade no contexto de bancos de dados? (Defina
escalabilidade vertical e horizontal)

Definição: Aumento da capacidade do mesmo servidor onde o banco de dados está instalado, por meio da adição de CPU, memória RAM, SSDs mais rápidos, etc.

https://blog.grancursosonline.com.br/escalabilidade-horizontal-e-vertical-em-bancos-de-dados-relacionais-e-nosql/

6 - Qual a relevância de organizar corretamente os dados em bancos
relacionais? (Explique a importância da estruturação/normalização)

A normalização de dados é fundamental para bancos de dados e empresas devido ao seu impacto na comunicação eficaz, na tomada de decisões e na usabilidade geral das informações. Dados des organizados e não normalizados apresentam desafios que dificultam a compreensão humana e das máquinas.

https://blog.invgate.com/pt/normalizacao-de-dados


7 - Como escolher entre SQL e NoSQL para um novo projeto? (Critérios para
decisão entre os modelos)

A principal diferença entre SQL e NoSQL está na forma como armazenam e consultam dados. O SQL utiliza uma linguagem estruturada de consultas, criada na década de 1970, ideal para trabalhar com dados organizados em tabelas. Já o NoSQL é mais recente e não possui uma linguagem de consulta padrão, usando geralmente documentos JSON. Ele oferece diferentes modelos, como chave-valor, colunas largas e grafos. Enquanto o SQL exige domínio da linguagem para manipular dados, o NoSQL permite interações mais flexíveis. Essa flexibilidade proporciona maior liberdade e criatividade na forma de gerenciar as informações.

https://www.astera.com/pt/knowledge-center/sql-vs-nosql/


# Comandos SQL

1 - Qual é a finalidade do comando SELECT em SQL? (Descreva sua função
e uso básico)

DML = Linguagem de Manipulação de Dados.
Adiciona, edita e remove dados, mas não os objetos que gerenciam e contêm dados. INSERT/UPDATE/DELETE/SELECT, também conhecido como CRUD, significa Criar, Ler, Atualizar e Excluir.

2 - O que significam as siglas DML e DDL em bancos de dados? (Defina e
diferencie Data Manipulation Language e Data Definition Language)

 DDL = Linguagem de Definição de Dados.
É o código que você usa para CRIAR ou ALTERAR uma tabela/visão/procedimento/etc.

https://www.quora.com/Can-you-explain-the-differences-between-DDL-DML-and-TCL-commands-in-SQL-Server-Which-command-is-used-for-creating-tables#:~:text=DDL%2C%20DCL%20e%20DML%20s%C3%A3o,Espero%20que%20ajude.&text=Todos%20estes%20s%C3%A3o%20comandos%20SQL,Exemplo:%20Conceder%2C%20Revogar.


3 - Para que serve a cláusula WHERE em consultas SQL? (Explique seu
papel na filtragem de dados)

O comando WHERE em SQL é uma cláusula usada para especificar condições que limitam o conjunto de registros a serem afetados ou retornados por uma operação de banco de dados, como SELECT, UPDATE ou DELETE. Sem o uso do WHERE, operações aplicar-se-iam a todas as linhas da tabela, o que raramente é desejado.


https://didatica.tech/para-que-serve-e-como-usar-o-comando-where-em-sql/


4 - Por que é fundamental estabelecer uma chave primária (PRIMARY KEY)
em tabelas? (Importância da chave primária)

As chaves primárias desempenham um papel importante em bancos de dados relacionais, reforçando a integridade dos dados e permitindo a recuperação bem-sucedida de dados. Além disso, as chaves primárias podem ser referenciadas por outro tipo de chave para definir relações entre tabelas em bancos de dados relacionais.

https://www.ibm.com/br-pt/think/topics/primary-key#:~:text=As%20chaves%20prim%C3%A1rias%20desempenham%20um,em%20bancos%20de%20dados%20relacionais.


5 - Como funciona o comando UPDATE e qual sua sintaxe básica? (Explique
a atualização de registros)

Para resolver esta falha de escrita podemos executar o comando SQL a seguir:

UPDATE
  produtos
SET
  descricao = 'Lápis preto (unid)'
WHERE
  id = 2

  https://www.devmedia.com.br/sql-update/41185

  6 - Qual a função do comando DELETE em SQL? (Diferença entre DELETE e
DROP)

O comando DROP TABLE exclui por completo uma tabela do banco de dados.

O comando DELETE exclui apenas os registros armazenados em uma tabela do banco de dados.

https://cursos.alura.com.br/forum/topico-diferenca-do-delete-para-o-drop-139817#:~:text=Garanta%20sua%20matr%C3%ADcula%20hoje%20e%20ganhe%20+%202%20meses%20gr%C3%A1tis&text=Ol%C3%A1%20Gabriel%2C%20tudo%20bem?,tabela%20do%20banco%20de%20dados.


7 - Como a cláusula ORDER BY organiza os resultados de uma consulta?
(Ordenação ascendente e descendente)

ORDER BY organiza os resultados de acordo com uma ou mais colunas da tabela, podendo definir a ordem do resultados como crescente ou decrescente.

https://www.devmedia.com.br/sql-order-by/41225#:~:text=ORDER%20BY%20organiza%20os%20resultados,resultados%20como%20crescente%20ou%20decrescente.&text=SQL:%20Order%20by-,ORDER%20BY%20organiza%20os%20resultados%20de%20acordo%20com%20uma%20ou,(ASC)%2C%20por%20padr%C3%A3o.

8 - Para que serve o comando LIMIT em consultas SQL? (Controle de
quantidade de registros retornados)

IMIT é uma cláusula SQL que especifica o número de linhas que devem ser retornadas no resultado de uma consulta.

Este recurso não está disponível em todos os SGBDS, como alternativa podem ser utilizadas as cláusulas TOP para SQL Server, ROWNUM para Oracle e FIRST para Firebird.

https://www.devmedia.com.br/sql-limit/41216

# Outros Conceitos

1 - Por que é importante integrar o banco de dados com a camada de backend da aplicação? (Relação entre BD e servidor)

O backend é um componente essencial da arquitetura de software que lida com o processamento de dados e a lógica de negócios, garantindo a funcionalidade e o desempenho gerais de um aplicativo e, ao mesmo tempo, mantendo os dados seguros e fornecendo uma base para a interação da interface de usuário do front-end.

https://www.couchbase.com/blog/pt/a-guide-to-backend-databases/#:~:text=O%20processamento%20no%20lado%20do,consultas%20para%20manipular%20os%20dados.

2 - O que são views (visões) em bancos de dados e quais suas vantagens?
(Conceito e utilidade de views)


O que são Views no SQL?
Uma view é uma representação virtual de uma tabela em um banco de dados. Ela não armazena dados fisicamente, mas é uma consulta predefinida que pode ser tratada como uma tabela em si. Basicamente, uma view é uma maneira de encapsular uma consulta complexa em uma estrutura mais simples e facilmente utilizável.

https://medium.com/@flaviagaia/criando-e-utilizando-views-no-sql-simplificando-consultas-e-melhorando-a-produtividade-eae5144f036b


3 - Quais são as propriedades ACID e por que são cruciais para
transações? (Atomicidade, Consistência, Isolamento, Durabilidade)

ACID é a sigla para Atomicidade, Consistência, Isolamento e Durabilidade. Essas são quatro propriedades essenciais que a maioria dos sistemas de gerenciamento de bancos de dados (DBMS, do inglês DataBase Management Systems) oferece como garantia ao lidar com transações.

A maioria dos DBMS populares, como MySQL, PostgresSQL e Oracle, possui garantias ACID prontas para uso. Outros têm garantias ACID parciais, como Redis, DynamoDB e Cassandra. A tendência, no entanto, parece ser que mais e mais DBMS ofereçam conformidade com ACID.

https://www.freecodecamp.org/portuguese/news/bancos-de-dados-acid-atomicidade-consistencia-isolamento-e-durabilidade-explicados/

4 - O que estabelece o Princípio do Privilégio Mínimo em segurança de
bancos de dados? (Conceito de menor privilégio e suas aplicações)


O princípio do menor privilégio consiste em conceder às identidades apenas os direitos de acesso específicos de que necessitam — nem mais, nem menos. Por exemplo, um analista financeiro pode precisar de acesso ao software de relatórios financeiros, mas não aos registros de RH. Isso reduz a probabilidade de exposição não autorizada de dados e limita o impacto de contas comprometidas.

https://netwrix.com/pt/cybersecurity-glossary/architectural-concepts/least-privilege/



