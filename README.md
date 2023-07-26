
# TallyAccounts

**TallyAccounts Software**

TallyAccounts, an integral part of the Voucher Automation Software Suite, is a powerful application developed using Python and integrated with MongoDB Atlas. This innovative software optimizes financial management by efficiently processing approved vouchers and initiating payments while ensuring strict adherence to a streamlined workflow.

*NOTE: You have to be connected to the internet for this application to work.

### Softwares:

1. [TallyMain](https://github.com/jaypunekar/AutoVoucherTally)
2. [TallyClient](https://github.com/jaypunekar/TallyClient)
3. [TallyAccounts](https://github.com/jaypunekar/TallyAccounts)

## Contents

- [Overview](#overview)
- [TallyAccounts Setup](#tallyaccounts-setup)
- [Installation](#installation)
- [Packaging](#packaging-the-application)
- [Screenshots](#screenshots)


## Overview
**Key Features of TallyAccounts**
1. **Payment Authorization:** TallyAccounts enforces payment authorization by requiring the upload of the payee's signature before initiating any payment. This additional layer of security ensures that payments are made only to authorized recipients, minimizing potential errors or unauthorized transactions.

2. **Voucher Integration with Tally ERP 9:** Once the voucher status is set to "paid" in TallyAccounts, the approved voucher data can be seamlessly integrated into Tally ERP 9 using TallyMain. This integration ensures real-time updates in the accounting system, maintaining accurate and up-to-date financial records.

3. **Voucher Selection Criteria:** TallyAccounts intelligently filters vouchers based on their approval status, processing only those vouchers that have been approved by TallyMain. This helps maintain a clear separation between approved and pending vouchers, streamlining the payment process and avoiding any confusion.

4. **Automated Payment Processing:** With a focus on efficiency, TallyAccounts automatically initiates payments for the selected vouchers. Whether it's online fund transfers, generating checks, or recording cash payments in Tally ERP 9, the app handles the payment process seamlessly.

5. **Status Tracking:** The software provides comprehensive tracking of payment statuses, ensuring complete visibility into the payment workflow. This allows users to monitor the progress of payments and manage financial obligations effectively.

TallyAccounts streamlines the payment processing for approved vouchers, safeguarding against unauthorized payments and ensuring accurate financial transactions. By effectively integrating with Tally ERP 9 through TallyMain, the software ensures a seamless flow of financial data, supporting businesses in maintaining a robust and efficient accounting system.


## TallyAccounts Setup


You can get all the files for the project by cloning the project repository.

```bash
  git clone https://github.com/jaypunekar/TallyAccounts.git
```
Go to the project directory
```bash
  cd TallyAccounts
```

You will get all the files in AutoVoucherTally directory.

Step 1: There are two files that contains the code we are concerned with. i.e. main.py and util.py. In both the files you will find a section right after imports where the code to connect to MongoDB database is there.

[![mongoinside.png](https://i.postimg.cc/G2yVQcrs/mongoinside.png)](https://postimg.cc/S2mgQbny)

Setep 2: Change the mongo_url to the url you got earlier while setting up MongoDB Atlas. And change the database name and collection name as well (You should have all of it if you have followed the MongoDB Atlas Setup section). Change the code in both (main.py & util.py) the files.

*NOTE:- Keep localhost as it is.
## Installation
### Software Requirement.

1. [TallyClient](https://github.com/jaypunekar/TallyClient)
2. [TallyAccounts](https://github.com/jaypunekar/TallyAccounts)
3. [TallyMain](https://github.com/jaypunekar/AutoVoucherTally)

You should have already run first two command if you followed [TallyAccounts Setup](#tallyaccounts-setup)

Clone the project:

```bash
  git clone https://github.com/jaypunekar/TallyAccounts.git
```
Go to the project directory
```bash
  cd TallyAccounts
```

Create conda virtual enviornment (This step in not necessory):
```bash
conda create -p venv python==3.8 -y
```
```bash
conda activate venv/
```

OR 
```bash
conda activate venv
```
Install dependencies:
```bash
pip install -r requirements.txt
```
#### Complete MongoDB Atlas and AutoVoucherTally Setup first else the following command won't work.

To run the program using Terminal:
```bash
python main.py
```
OR
```bash
python3 main.py
```


## Packaging the Application

In the Terminal (In TallyAccounts dir) run:
```bash
pyinstaller --onefile main.py  
```

Then run:

```bash
pyinstaller --name TallyAccounts --onefile --windowed --main.py
```

If you want to add an icon run (icon.ico should be in TallyAccounts dir):
```bash
pyinstaller --name TallyAccounts --onefile --windowed --icon=icon.ico --main.py
```
#### You will see a "dist" folder in TallyAccounts directory. Inside the "dist" folder you will get the executable file.

## Screenshots
[![img1.png](https://i.postimg.cc/2yTRkqfd/img1.png)](https://postimg.cc/wRtbFjM3)

[![img-2.png](https://i.postimg.cc/fyHzHqkh/img-2.png)](https://postimg.cc/64vxq0dH)
