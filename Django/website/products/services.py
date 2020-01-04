from products.models import Design
from django.core.files.storage import FileSystemStorage
import base64
from django.core.files.base import ContentFile
def saveDesignCoordinate(design,imageData,art_top,art_left,art_height,art_width,frame_top,frame_left,frame_width,frame_height,frame_border_radius,
frame_rotation,text_font,text_top,text_left,text_weight,text_style,text_color,text_size,text):

    imageData = imageData
    format, imgstr = imageData.split(';base64,')
    ext = format.split('/')[-1]
    imageData = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    fileStorage = FileSystemStorage()
    fileStorage.location = 'media/design_pics'
    if design.design_photo.url != '/media/design_pics/defaultDesign.png':
        storage, path = design.design_photo.storage, design.design_photo.path
        storage.delete(path)
    name = fileStorage.get_available_name('design.png')
    fileStorage.save(name,imageData)
    design.design_photo = 'design_pics/'+name

    ##art
    design.designArtCoordinate.coordinate_top = art_top
    design.designArtCoordinate.coordinate_left = art_left
    design.designArtCoordinate.height = art_height
    design.designArtCoordinate.width = art_width
    ##artframe
    design.designArtFrameCoordinate.frame_coordinate_top = frame_top
    design.designArtFrameCoordinate.frame_coordinate_left = frame_left
    design.designArtFrameCoordinate.frame_width = frame_width
    design.designArtFrameCoordinate.frame_height = frame_height
    design.designArtFrameCoordinate.frame_border_radius = frame_border_radius
    design.designArtFrameCoordinate.rotation = str(frame_rotation)
    ##text
    design.designTextCoordinate.font = text_font
    design.designTextCoordinate.font_weight = text_weight
    design.designTextCoordinate.font_style = text_style
    design.designTextCoordinate.coordinate_top = text_top
    design.designTextCoordinate.coordinate_left = text_left
    design.designTextCoordinate.font_color = text_color
    design.designTextCoordinate.text = text
    design.designTextCoordinate.font_size = text_size

    design.designArtCoordinate.save()
    design.designArtFrameCoordinate.save()
    design.designTextCoordinate.save()
    design.save()

def deleteDesign(designPk):
    design = Design.objects.get(id= designPk)
    storage, path = design.design_photo.storage, design.design_photo.path
    design.delete()
    storage.delete(path)
