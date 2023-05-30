# SematicDemo

This is an example Sematic project, which was generated using `Sematic 0.27.0` for [this article](https://medium.com/@hqcharlyjin/sematic-an-open-source-development-platform-for-mlops-c71a5182b551)

Take a look at the [Sematic documentation](https://docs.sematic.dev/onboarding/readme) to get started.

## How to install
You need to install libmagic on your computer:

MacOs: brew install libmagic, or port install file
Debian: sudo apt-get install libmagic1
RPM: sudo yum install file-devel
Windows unofficial support: pip install python-magic-bin

To install sematic, run:
```
pip install sematic
```

Install Dependencies with 
```
pip install -r requirements.txt
```

## How to run

Start the sematic dashboard with 
```
sematic start
```

Run the code for SVD with 8 features with 
```
python3 -m movie_rec --features 8
```

Stop the sematic dashboard with 
```
sematic stop
```
