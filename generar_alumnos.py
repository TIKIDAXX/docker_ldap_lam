# Generar archivo LDIF con 472 alumnos
with open("alumnos.ldif", "w") as f:
    for i in range(2, 474):
        f.write(f"""dn: cn=alumno{i} alumno,cn=alumnos,ou=alumnos,dc=rais,dc=org
givenName: alumno{i}
sn: alumno
cn: alumno{i} alumno
uid: aalumno{i}
userPassword: alumno
uidNumber: {1000 + i}
gidNumber: 500
homeDirectory: /home/users/aalumno{i}
loginShell: /bin/bash
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: top

""")

print("✅ Archivo alumnos.ldif generado con éxito.")
