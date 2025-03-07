"""
touch <nombre del archivo>.<extension del archivo>
comando usado para crear archivos dentro de la carpeta en la que nos encontremos mediante la ocnsola de la gitbash

git config --global user.name "<nombre de usuario dueño del repositorio (usuario de github ejemplo)>"
comando usado para asignar el nombre de usuario identificador del repositorio local, recomendablemente debe ser el mismo que de el entorno gitub

git config --global user.email <Correo electronico del repositorio local(email del github ejemplo)>
comando usado para asignar el correo electronico que sera utilizado para identificar quien modifico algo en el repositorio

para confirmar si se crearon correctamente se usan los comandos
git config user.name
git config user.email

o viendo el archivo gitconfig que se encuentra dentro del sistema mayormente encontrado en la carpeta de usuario del equipo.

git init
comando utilizado para inicializar el repositorio en la carpeta actual (volviendolo un repositorio git)

para Hacer que un archivo del proyecto este listo para subirse en el siguiente commit se utiliza:
git add <nombre del archivo> o git add .

Nota:[
    en caso de que se escriba o modifique cualquiera de los archivos añadidos, su estado cambiara a Modified, es decir modificado
    donde se ah de retornar si estado volviendolo en untracked
]

En caso de que el archivo que se volvio added y esta en zona de preparacion se requiera retornar a su estado anterior se utiliza el comando:
git rm --cached index.html

si el archivo posterior a estar added fue modificada te marcara un error 
donde para retornar al estado U, se debe de forzarlo con -f despues del cached

git rm --cached -f <nombre del archivo>.<extension del archivo>

donde se puede usar git add a cada archivo modificado o a todos con el:
git add .


------------------commit--------------------------------------
git commit -m "<mensaje de commit>"

como los commit son adiciones al repositorio, es muy recomendable que el mensaje sea alucivo al cambio realizado en ese commit,
algo muy puntual
---------------------------------------------------------------
----------------------tag-------------------------------------
git tag <nombre identificador de la etiqueta>

como son muchos los valores numericos identificadores para saber cual es el commit realizado,
cuando se valla a realizar una accion se requiere de utilizar una etiqueta {tag} la cual funcionara como
el nuevo identificador del commit y asi no perderse con la identificacion numerica.
---------------------------------------------------------------
----------------log---------------------------------------------

git log

con este comando se vera el historia de los commit ejecutados en el repositorio, con su hash y la cabesera, identificando en que
commit o version del proyecto nos encontramos, si regresamos aun commit anterior, la cabesa head indicara que estamos ahi.
ademas que posterior a la head con una flecha indica en que rama nos encontramos.
incluyendo el author del commit, la fecha y el comentario.

hay variaciones del git log, segun se quiera, como:
git log --oneline

que te resume el hash en solo 7digitos, te muetra donde esta la cabeza, en que rama se encuentra y el comentario puesto al commmit

git log --graph
util cuando se trabaja en varias ramas y en distintas versiones o commits, ya que te indica

git lo --stat
que muestra los cambios realizados en el commit

estos se pueden conbinar para para mostrar de la manera en que queremos visalizar el log o historial.

git reflog
comando usado para mostrar el historial completo de commits realizados sin importar en que rama , version o commit nos
encontremos.

--------------------------------------------------------------------------
------------------diferencias entre commit-----------------------------------------------------------
git diff <nombre de la primera etiqueta a comparar> <nombre de la segunda etiqueta a comparar>

usado este comando para ver cuales son los cambios realizados entre el un commit y otro commit mediante sus
etiquetas

------------------------------------------------------------------------------------------------
--------------cambiar de version o de commit----------------------------------------------

git checkout <hash identificador del commit o etiqueta del commit>

esto para usado mas que nada para visualizar el estado 

para voolver a cambiar de version se hace el mismo comando 
pero se debe de cambiar la rama en la que se esta trabajando
por que al hacer checkout cambiamos de commit y trabajamos en un commit
no en una rama como tal
se utiliza:
git switch <nombre de la rama a cambiar, la principal puede ser o master o main>

----------------------------------------------------------------------------------------------------------------------
--------------------revertir un commit------------------------------------------------------------
git revert HEAD

este comando te manda a una ventana donde deberias de colocar por que revertiste el commit
se utiliza para revertir el ultimo commit realizado , es decir, los avances realizados desde hasta el ultimo commit hecho

git revert HEAD --no-edit

añadiendo el --no-edit hace que se ejecute el comando sin necesidad de ingresarle texto explicando por que se revertio el commit


--------------------------------------------------------------------------------------------------------------------
---------------------------------actualizar un commit--------------------------------------------------------------
se utiliza el --amend para realizar un commit sobre el ultimo ya realizado

git commit --amend -m "mensaje de la actualizacion"


-------------------------------------------------------------------------------------------------------------------
---------------------------ramas en git----------------------------------------------------------------------------

git branch <nombre de la rama>
con este comando se pueden crear ramas nuevas con las que poder trabajar sin afectar la principal

git branch
con este comando se pueden ver todas las ramas que existen en el proyecto y en la que este puesto un asterisco ,
es por que esa es la rama en la que te encunetras en este momento

git switch <nombre de la rama a cambiar>
con este comando se puede cambiar de rama y trabajar en ella

git checkout -b <nombre de la nueva rama>
con este comando puedes crear una rama nueva y de una vez pasar a trabajar en ella sin hacer el switch

git merge <nombre de la rama con la que se quiere fusionar >
con este comando se puede fusionar la rama en la que se esta trabajando con otra rama como la principal,
esto se hace mas que nada cuando se comprueba que no hay fallas en la rama trabajada, y se puede actualizar
la principal con los cambios realizados en la otra rama

git branch -d <nombre de la ramaa que se quiere eliminar>
con este comando se puede eliminar una rama que ya no se necesita, se recomienda hacer esto despues de fusionar las ramas para no 
crear demasiadas ramas en el repositorio que queden inutilizables.

===================================================================================================================

---------------------------------github----------------------------------------------------------------------------
primero Se crea el nuevo repositorio en la pagina de github
colocando:
- el nombre del repositorio (recomendablemente un nombre corto y preciso, si tiene espacios, estos se sustituyen por guion bajo)
- una descripcion del repositorio , algo para saber que tendra el repositorio
- si se quiere que el repositorio sea publico o privado
- si se quiere que el repositorio tenga un licencia(no toquemos esto de momento)
- si se quiere que el repositorio tenga un README.md (recomendablemente siempre tengamos uno)
- si se quiere que el repositorio tenga un .gitignore (se deja en non mayormente si es publico, y en caso de privado si se sabe que tipo de archivo no estara en el repositorio)

para colonar el repositorio se le da a add file y ahi donde dice clone en https copiamos la ruta generada,
colocamos en el git de visual studio el comando
git clone <la direccion https generada>
con este comando se puede clonar el repositorio en el equipo local






====================================================================================================================





"""