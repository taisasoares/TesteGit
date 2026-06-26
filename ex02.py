def descendentes(a):
    if a[1] == []:
        return []
    else:
        return [nm for nm, _ in a[1]] + [nm for f in a[1] for nm in descendentes(f)]

arv = (
    "Maria",
    [
        ("Joana", [
            ("Lucio", []),
            ("Jõao", [])
        ]),
        ("Pedro", []),
        ("Patricia", [
            ("Marina", [
                ("Marcelo", []),
                ("Tomás", [])
            ])
        ]),
        ("Marcos", [])
    ]
)

print(descendentes(arv))