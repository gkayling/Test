# Much of this logic can be performed on one line, but I split it up to allow
# for easier understanding and so I could add more detailed comments.

def spiral(grid):
  retVal = []
  if(grid):
    retVal = list((grid)[0])             # Get the top row of the grid
    nextGrid = grid[1:]                  # No longer need top row
    nextGrid = reversed(zip(*nextGrid))  # Transpose grid, reverse list order
    retVal += spiral(list(nextGrid))     # Recursively call until no more grid
  return retVal  

def formatBlock(block):  
  block = block.strip().replace(' ', '') # Remove all whitespace
  block = block.replace('\n\n', '\n')    # Allow newline to delimit rows 
  rowArray = block.split('\n')           # Get a list of the rows
  grid = []                              # Create a 2D list for the block
  for i in range(0, len(rowArray)):
    grid.append([]);
    for j in range(0, len(rowArray[0])):
      grid[i].append(rowArray[i][j])     # Fill in the corresponding values      
  return spiral(grid)  

#Main#
f = open('input.txt', 'r')               # Open source file
text = f.read().strip()                  # Remove leading/trailing empty space

blockArray = text.split('\n\n\n')        # Delimited by two empty lines
outputString = ''
for block in blockArray:
  outputString += ','.join(formatBlock(block)) + "\n\n"
f = open('output.txt', 'w')  
f.write(outputString)                    # Write result to file

