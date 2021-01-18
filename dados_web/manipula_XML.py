import xml.dom.minidom


def manipula_xml():
    doc = xml.dom.minidom.parse(
        "//home//igor//projetos_pessoais//curso_python_linkedin//dados_web//exemploXML.xml"
    )

    print("Nome da primeira tag" + str(doc.firstChild.tagName))
    primeiroNome = doc.getElementsByTagName("firstname")
    print(primeiroNome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName("skill"):
        print("Skill encontrado: ", skill.getAttribute("name"))


manipula_xml()
