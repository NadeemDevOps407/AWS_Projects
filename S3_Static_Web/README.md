## Hosting a Static Website on Amazon S3

In this guide, we will walk you through the process of hosting a static website on S3. By following these steps, you will be able to create an S3 bucket, upload your website files, configure the bucket for website hosting, and make your website publicly accessible.

#### Step 1: Sign in to AWS

    Open a web browser click (https://aws.amazon.com/console).
    AWS account credentials to sign in.

#### Step 2: Create an S3 Bucket

    In the AWS Management Console, search for "S3" in the search bar and click on "Amazon S3" under the Storage category.
    Click on the "Create bucket" button.
    Enter a unique name (e.g., "my-website1007").
    Choose the AWS Region (e.g., US East (N. Virginia)).
    Leave the default settings for the remaining options and click on the "Create bucket" button.

#### Step 3: Upload Your Website Files to the S3 Bucket

    In the bucket overview page, click on the "Upload" button.
    Click on the "Add files" button and select the HTML files that make up your website.
    Click on the "Next" button.
    Leave the default settings for permissions and other options.
    Click on the "Upload" button to start uploading your website files to the S3 bucket.

#### Step 4: Configure the S3 Bucket for Website Hosting

    After the files have finished uploading, go to the bucket overview page.
    Click on the "Properties" tab.
    Scroll down to the "Static website hosting" section and click on the "Edit" button.
    Select the "enable web hosting" option.
    Enter the name of the index document for your website (e.g., "index.html").
    Click on the "Save changes" button.

#### Step 5: Make Your Website Publicly Accessible

    In the bucket overview page, go to the "Permissions" tab.
    Under the "Block public access" section, click on the "Edit" button.
    Uncheck all the options to allow public access to your website.
    Click on the "Save changes" button.

#### Step 6: Make the Website Files Public

    In the bucket overview page, go to the "Objects" tab.
    Select the HTML files you uploaded for your website.
    Click on the "Actions" button and choose "Make public using ACL".
    Confirm the action to make the selected files public.

####S Step 7: Access Your Website

    In the bucket overview page, go back to the "Properties" tab.
    Under the "Static website hosting" section, you will find the website endpoint URL.
    Copy the endpoint URL and paste it into a web browser.
    Your website should now be accessible to the public.

Conclusion:
Congratulations! You have successfully hosted your static website on Amazon S3. By following the steps outlined in this guide, you were able to create an S3 bucket, upload your website files, configure the bucket for website hosting, and make your website publicly accessible. You can now share your website with others by providing them with the website endpoint URL.