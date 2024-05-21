import psycopg2


class ConexaoFactory:    
    def get_conexao(self):
        return psycopg2.connect(host='ep-flat-thunder-a4om8s0m.us-east-1.aws.neon.tech', database='2545SHIFT_DB', user='2545SHIFT_DB_owner', password='CBSb62cltinA')



    