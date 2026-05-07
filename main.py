class Kontekst:
    def __enter__(self):
        print("Kontekstga kirishmoqdamiz")
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print("Kontekstdan chiqib kelmokdamiz")

    def ishlayapmiz(self):
        print("Biz ishlayapmiz")

with Kontekst() as kontekst:
    kontekst.ishtirokchi = "Dasturchi"
    kontekst.ishlayapmiz()
```

```python
class Kontekst:
    def __enter__(self):
        print("Kontekstga kirishmoqdamiz")
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print("Kontekstdan chiqib kelmokdamiz")

    def ishlayapmiz(self):
        print("Biz ishlayapmiz")

try:
    with Kontekst() as kontekst:
        kontekst.ishtirokchi = "Dasturchi"
        kontekst.ishlayapmiz()
        raise Exception("Xatolik")
except Exception as e:
    print(f"Xatolik: {e}")
```

```python
class Kontekst:
    def __enter__(self):
        print("Kontekstga kirishmoqdamiz")
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print("Kontekstdan chiqib kelmokdamiz")

    def ishlayapmiz(self):
        print("Biz ishlayapmiz")

try:
    with Kontekst() as kontekst:
        kontekst.ishtirokchi = "Dasturchi"
        kontekst.ishlayapmiz()
        raise Exception("Xatolik")
except Exception as e:
    print(f"Xatolik: {e}")
    return False
```

```python
class Kontekst:
    def __enter__(self):
        print("Kontekstga kirishmoqdamiz")
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print("Kontekstdan chiqib kelmokdamiz")

    def ishlayapmiz(self):
        print("Biz ishlayapmiz")

try:
    with Kontekst() as kontekst:
        kontekst.ishtirokchi = "Dasturchi"
        kontekst.ishlayapmiz()
        raise Exception("Xatolik")
except Exception as e:
    print(f"Xatolik: {e}")
    return False
