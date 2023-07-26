
CREATE SEQUENCE IF NOT EXISTS experimento_id_seq;
CREATE TABLE IF NOT EXISTS experimento(
    id BIGINT NOT NULL default nextval('experimento_id_seq'),
    click INT NOT NULL,
    visit INT NOT NULL,
    grupo VARCHAR(30) NOT null,
    PRIMARY KEY(id)
    );
ALTER SEQUENCE experimento_id_seq
OWNED BY experimento.id;