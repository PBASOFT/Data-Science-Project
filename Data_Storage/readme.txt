
To run Neo4j container:

docker pull neo4j

docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    neo4j

---> put in a name:

docker run \
    --name hyped4neo --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    neo4j

------

username: neo4j
password: j4neo

port 7474:7474 
bolt://0.0.0.0:7687


TUTORIAL: https://www.youtube.com/watch?v=8OeTZYTMZgc