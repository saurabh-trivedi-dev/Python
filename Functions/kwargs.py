# **kwargs keywords and arguments

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="Saurabh", job="Developer", company="HCLTech")
print_kwargs(name="Tanish", company="Infosys")
print_kwargs(job="GET", company="Fujitsu")
print_kwargs(name="Aum", country="Australia", work="Warehouse")