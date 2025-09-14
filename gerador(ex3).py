import random
import string

todos = string.ascii_letters + string.digits + "!@#$%&*"

antes = ''.join(random.choice(todos) for _ in range(6))

depois = ''.join(random.choice(todos) for _ in range(7))

senha = antes + "Roberto" + depois

print("Senha:", senha)
