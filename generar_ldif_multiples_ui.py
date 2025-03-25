def genera_contenido_ldif_multiples_unidades_organizativas(filename, lista_ou_name, base_dn):
    """Genera un archivo LDIF con múltiples unidades organizativas."""
    ldif_content = ""
    
    for ou_name in lista_ou_name:
        ldif_content += f"""
# Organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}
"""
    
    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Lista inicial de unidades organizativas
# Parámetros
base_dn = "dc=rais,dc=org"    # Base DN tomado del docker-compose
lista_ou_name_1 = [
    "directores", "profesores", "alumnos"
]
#genera_contenido_ldif_multiples_unidades_organizativas("filename1.ldif", lista_ou_name, base_dn)
# Lista extendida con más unidades organizativas
lista_ou_name_2 = [
    "personalnodocente", "eso1", "eso2", "eso3", "eso4",
    "bach1ciencias", "bach1humanidades", "bach2ciencias", "bach2humanidades",
    "profesoreseso", "profesoresbach", "profesoreseso1", "profesoreseso2",
    "profesoreseso3", "profesoreseso4", "profesoresbach1ciencias",
    "profesoresbach1humanidades", "profesoresbach2ciencias", "profesoresbach2humanidades"
]
genera_contenido_ldif_multiples_unidades_organizativas("filename2.ldif", lista_ou_name_2, base_dn)



# Instrucciones para importar el LDIF en OpenLDAP
'''def importar_ldif_en_openldap(ldif_file):
    import os
    
    command = f"docker cp {ldif_file} openldap:/tmp/{ldif_file} && " \
              f"docker exec -it openldap ldapadd -x -D 'cn=admin,{base_dn}' -w admin -f /tmp/{ldif_file}"
    
    os.system(command)
    print(f"Archivo {ldif_file} importado en OpenLDAP.")

# Importar automáticamente el archivo generado en OpenLDAP
importar_ldif_en_openldap(filename)

'''

