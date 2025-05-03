# **<u> Wordle Ruiner </u>**

A made this to ruin my friend's days and text them the Wordle answer before they got the chance to do it themselves. I know this is evil, but I think it's kinda funny and turned it off once they figured out it was me.

___
## **<u> Running the script </u>**

To run WordleRuiner, you'll need two files that are included in the `.gitignore`:

* `email.txt`
* `pass.txt`

These will include an email account and application password to said email account that you control, this is what will send the texts.

I followed [this guide](https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4) on setting up my email accounts permissions and generating the application password.

You can hard code in the victims you want to send the Wordle word to by setting the `victims` array on Line 21 of `main.py`. You'll need to know their number and their cell phone carrier.

Each element of the array should be a tuple of the form:

`("phone number \<XXXXXXXXXX>", "carrier-code")`

The carrier codes for a few common carriers are as follows:

* `Verizon`: `verizon`
* `AT&T` : `att`
* `T-Mobile`: `tmobile`
* `Sprint`: `sprint`

Then just run the script with `python main.py`

Alternatively, you can pass in victim numbers and carriers via the command line.

Example: `python main.py 1234567890 verizon 0987654321 att`

The script will run continously, checking every hour to see if the Wordle word has updated and sending a new text to all victims if it has.

Have fun and I'm sorry.