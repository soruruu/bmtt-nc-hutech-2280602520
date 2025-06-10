openssl req -new -x509 -newkey rsa:2048 -nodes -keyout server.key -out server.csr -days 365 -config server-cert.cnf
