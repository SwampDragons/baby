# baby

An easy tool for announcing your baby's arrival!

# Usage

A simple use is to give it a JSON formatted data set to work with at a given
url.  Here is a sample file:


```json
{"parents": ["Alice", "Bob"]}
```

Pass the url to the class:

```py
>>> from baby import Baby
>>> url = 'https://www.example.com/baby'
>>> b = Baby(url)
>>> b.announce()
Alice and Bob are excited to announce the impending arrival of a baby
```

You can include other information.  Each of the following values are strings so
feel free to use anything you want here.

- sex: "girl", "boy", "other"
- name: "Claire", "Dave", ..... good luck, this one's hard
- due_date: "January 15, 2015" or in unix time "1440646846"

# Future Releases

- Delivery date announcement
