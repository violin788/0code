const fs = require('fs');
const { Octokit } = require('@octokit/rest');

// Initialize Octokit with your GitHub personal access token
const octokit = new Octokit({
  auth: 'YOUR_PERSONAL_ACCESS_TOKEN'
});

// Specify the owner and name of the repository
const owner = 'owner_username';
const repo = 'repository_name';

// Specify the file path and content
const filePath = 'path/to/your/file.txt';
const fileContent = 'Content of your file';

// Function to commit a file
async function commitFile() {
  try {
    // Get the current commit reference
    const { data: { object: { sha } } } = await octokit.git.getRef({
      owner,
      repo,
      ref: 'heads/master' // Specify the branch name
    });

    // Get the current tree
    const { data: tree } = await octokit.git.getTree({
      owner,
      repo,
      tree_sha: sha,
      recursive: true
    });

    // Create a new blob with the file content
    const { data: { sha: blobSha } } = await octokit.git.createBlob({
      owner,
      repo,
      content: fileContent,
      encoding: 'utf-8'
    });

    // Create a new tree with the updated file
    const newTree = tree.tree.map(item => ({
      ...item,
      path: item.path === filePath ? filePath : item.path,
      sha: item.path === filePath ? blobSha : item.sha
    }));

    // Create a new tree in the repository
    const { data: newTreeResult } = await octokit.git.createTree({
      owner,
      repo,
      tree: newTree
    });

    // Create a new commit
    const { data: newCommit } = await octokit.git.createCommit({
      owner,
      repo,
      message: 'Commit via Octokit',
      tree: newTreeResult.sha,
      parents: [sha] // Specify the parent commit
    });

    // Update the reference to point to the new commit
    await octokit.git.updateRef({
      owner,
      repo,
      ref: 'heads/master', // Specify the branch name
      sha: newCommit.sha
    });

    console.log('File committed successfully!');
  } catch (error) {
    console.error('Error committing file:', error.message);
  }
}

// Call the function to commit the file
commitFile();
