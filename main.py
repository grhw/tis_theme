import cssutils
import generate

sheet = cssutils.parseString("\n".join(generate.compiled))

rules_dict = {}

for rule in sheet:
    if isinstance(rule, cssutils.css.CSSStyleRule):
        declarations = tuple(sorted([(decl.name, decl.value) for decl in rule.style]))
        
        if declarations in rules_dict:
            rules_dict[declarations].append(rule.selectorText)
        else:
            rules_dict[declarations] = [rule.selectorText]

compressed_css = ""
for declarations, selectors in rules_dict.items():
    selector_text = ', '.join(selectors)
    properties = ' '.join([f"{name}: {value};" for name, value in declarations])
    compressed_css += f"{selector_text} {{{properties}}}\n"

theme_css = ""
with open("src/fonts.css","r") as f:
    theme_css = f.read() + "\n" + compressed_css

with open("theme/tis.theme.css","w+") as f:
    f.write(theme_css)