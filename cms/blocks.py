from wagtail.core import blocks
from wagtail.core.blocks import CharBlock
from wagtail.images.blocks import ImageChooserBlock


class InlineImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(label=("Image"))
    caption = CharBlock(required=False, label=("Caption"))
    float = blocks.ChoiceBlock(
        required=False,
        choices=[('right', ("Right")), ('left', ("Left")), ('center', ("Center"))],
        default='right',
        label=("Float"),
    )
    size = blocks.ChoiceBlock(
        required=False,
        choices=[('small', ("Small")), ('medium', ("Medium")), ('large', ("Large"))],
        default='small',
        label=("Size"),
    )

    class Meta:
        icon = 'image'