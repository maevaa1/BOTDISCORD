
class Node :
    def __init__(self,question,keyword):
        self.question = question
        self.keyword = keyword
        self.list_child_node =[]

    def user_response(self):
        print(self.question)
        txt = input()
        for child in self.list_child_node:
           if child.keyword in txt:
              child.user_response()

    def insert(self, node, question):
        if self.question == question :
            self.list_child_node.append(node)
        else:
            for child in self.list_child_node:
                child.insert(node,question)




first_question_racine = "Quels sont vos besoins ? \n Insérez un des mots clès \n PDF \n Video "
question_one_pdf = "Quel pdf aurez-vous besoin ? \n Python \n Javascript"
question_one_video ="Quel video aurez-vous besoin \n Python \n Php \n Javacript "


tree = Node("Dites help pour commencer","aide")

tree.insert(Node(first_question_racine,"help"),"Dites help pour commencer")
tree.insert(Node(question_one_pdf,"PDF"),first_question_racine)
tree.insert(Node(question_one_video,"Video"),first_question_racine)


# choix reponse pdf
tree.insert(Node("Ecrivez : Python","Python"),question_one_pdf)
tree.insert(Node("Ecrivez : Javascript","Javascript"),question_one_pdf)

#choix reponse video
tree.insert(Node("Ecrivez : Python","Python"),question_one_video)
tree.insert(Node("Ecrivez : Php","Php"),question_one_video)
tree.insert(Node("Ecrivez : Javascript","Javacript"),question_one_video)


current_path = [tree]



                