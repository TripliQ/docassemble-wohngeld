# NRW Wohngeldantrag

![Wohngeld Logo](docassemble/wohngeld/data/static/welcome_screen.svg)

A [docassemble](https://github.com/jhpyle/docassemble) interview to easily create the NRW Wohngeldantrag via an online Interview.


## Installation and Usage

1. Navigate to the docassemble `Playground`
2. Click the `Pull` icon
3. Pull from the repository with the following `GitHub URL`
```
https://github.com/TripliQ/docassemble-wohngeld.git
```

## File/Folder Structure

```
├── docassemble                           # Main files for interview
    ├── wohngeld                          # Project name
        ├── data                          # All data files
            ├── questions                 # All question `yml` files
                ├── document.yml          # Logic for filling document pdf fields
                ├── interview.yml         # Main interview logic
                ├── questions.yml         # All questions asked during interview
                ├── review.yml            # Review screen questions
            ├── sources           
            ├── static                    # All static content such as pictures
            ├── templates                 # Templates to be filled
                ├── wohngeldantrag.pdf    # Main PDF form to be filled
├── LICENSE 
├── MANIFEST.in
├── README.md
├── setup.cfg                   
└── setup.py
```

## Authors

TripliQ

Legal Tech Lab Cologne
