#!/bin/bash

# Exit on error
set -e

# Variables
WIKI_REPO="git@github.com:CroodSolutions/CISOinaBox.wiki.git"
TMP_DIR="temp_wiki"

# Clone the wiki repository
echo "Cloning wiki repository..."
rm -rf $TMP_DIR
git clone $WIKI_REPO $TMP_DIR

# Enter the wiki directory
cd $TMP_DIR

# Clear existing content
echo "Clearing existing wiki content..."
find . -name "*.md" -type f -delete

# Generate a sidebar
echo "Generating sidebar..."
echo "### CISO in a Box" > _Sidebar.md
echo "" >> _Sidebar.md
echo "* [Home](Home)" >> _Sidebar.md
echo "* [Contributing](Contributing)" >> _Sidebar.md

# Copy and rename files
echo "Copying and renaming files..."
for dir in ../[0-9]*; do
  if [ -d "$dir" ]; then
    # Get the directory name without the path
    dir_name=$(basename "$dir")
    
    # Find the readme file (case-insensitive)
    readme_file=$(find "$dir" -maxdepth 1 -iname "Readme.md")

    if [ -f "$readme_file" ]; then
      # Create a wiki-friendly name
      wiki_name=$(echo "$dir_name" | sed 's/ /-/g' | sed 's/---/-/g')
      
      # Copy the file
      cp "$readme_file" "${wiki_name}.md"
      
      # Add to sidebar
      echo "* [${dir_name}](${wiki_name})" >> _Sidebar.md
    fi
  fi
done

# Copy contributing guide
if [ -f "../CONTRIBUTING.md" ]; then
  cp "../CONTRIBUTING.md" "Contributing.md"
fi

# Create a Home page
if [ -f "../Start Here.md" ]; then
  cp "../Start Here.md" "Home.md"
else
  echo "CISO in a Box" > Home.md
fi


# Commit and push changes
echo "Committing and pushing changes..."
git add .
git commit -m "Update wiki from repository"
git push origin master

# Clean up
echo "Cleaning up..."
cd ..
rm -rf $TMP_DIR

echo "Wiki update complete!"
