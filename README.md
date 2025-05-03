### Information

It is based on [GitHub Page](https://pages.github.com) and has the ability to sort and filter data through the use of [jQuery](https://jquery.com) and [DataTables](https://datatables.net).

#### File sharing & Cloud storage

* **File sharing** - only resources that do not require registration.
* **Cloud storage** - only resources with a free tariff unlimited in time of use (not trial).

### Contributions

* Fork this repository

Clicking on the `Fork` button on the top of this page. This will create a copy of this repository in your account.

* Clone the repository

Go to your GitHub account, open the forked repository, click on the `Clone or download` button and then click the copy to clipboard icon. Open a terminal and run the following git command:

`git clone <url repository>`

* Open a project in IDE or text editor

Recommendations: [IntelliJ IDEA Community](https://www.jetbrains.com/idea/), [Visual Studio Code](https://code.visualstudio.com) or [Sublime Text](https://www.sublimetext.com)

* Make changes to the file `spreadsheet.json`, for example:

```
{
    "Name": "<a href='https://dropmefiles.com'>DropMeFiles</a>",
    "Type": "File sharing",
    "Free volume": "50 GB",
    "Shelf life": "14",
    "Download count": "Yes",
    "Language": "English, Russian",
    "Application": null
}
```

* Commit the changes and push

```
git commit -m "Add <name cloud storage or file sharing>"
git push
```

* Submit your changes for review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

You will get a notification email once the changes have been merged.

* Synchronize your branch with this repository

Add the url of my repository to the field `upstream <remote url>`:

`git remote add upstream git@github.com:nafanz/nafanz.github.io.git`

Download the latest changes from my repository.

`git fetch upstream`

We are merging a new version of my repository with your master branch.

`git rebase upstream/master`

Pushing these changes to your GitHub repository.

`git push origin master`

* Profit

Keep track of the project and make new changes.
