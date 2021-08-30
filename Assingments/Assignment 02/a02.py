### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###

def calculateArea(width,length):
    area=width*length
    return area

#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###

def checkTilesFit(plot_width,plot_length,tile_width,tile_length):
    plotearea= plot_width*plot_length
    tilearea= tile_width*tile_length
    if plotearea%tilearea==0 and (plot_width%tile_width==0 or plot_width%tile_length==0) and (plot_length%tile_length==0 or plot_length%tile_width==0) and plot_width>0 and plot_length>0 and tile_length>0 and tile_width>0:
        return True
    else:
        return False
#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###

def calculateTiles(plot_width,plot_length,tile_width,tile_length):
    if type(plot_width)==str or type(plot_length)==str or type(tile_width)==str or type(tile_length)==str:
        return "Invalid Input"
    elif plot_width==0 or plot_length==0 or tile_width==0 or tile_length==0:
        return None
    if checkTilesFit(plot_width,plot_length,tile_width,tile_length)==True:
        Area_Tile=tile_width*tile_length
        Area_Plot=plot_width*plot_length
        TotalTiles=Area_Plot/Area_Tile
        print(TotalTiles)
        if TotalTiles / int(TotalTiles) == 1:
            return int(TotalTiles)
        else:
            return "Not Possible"
    else:
        return "Not Possible"

#### End OF MARKER



