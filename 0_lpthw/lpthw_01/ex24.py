print("let's print some interesting things")
print('You \' d need to know \' about escapes with \\ that do:')
print('\nNew lines and \t tabs.')


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from institution
and requires an explanation
\n\t\t where there is none
"""

print("-----------------------------")
print(poem)
print("-----------------------------")

five = 10-5
print(f"five is equal to: {five}")


def secret_formula(started):
    jelly = started * 500
    apples = jelly/10
    applepines = apples + 20
    return jelly,apples,applepines

strate_num = 1000
fruit1,fruit2,fruit3 = secret_formula(strate_num)
print(fruit1,fruit2,fruit3)

print("with a starting point with:{}".format(strate_num))
formula = secret_formula(strate_num)
print("we'd have {} jellys, {}apples, {}applepines".format(*formula))
