# FreeLighting

**Work in Progress: this page may be continuously updated and the model is also continuously updated.**

<!-- FreeLighting is a DIT-based relighting model to manipulate the illumination and background of images. Currently, FreeLighting contains two types of models: text-guided relighting model and image-guided relighting model. 

For text-guided relighting model, uploading a image, FreeLighting can relight the foreground object with background replace simultaneously according to a text prompt. Compare to existed relighting models, FreeLighting can better keep texture and intrinsic of original images. 

For image-guided relighting model, taking an original image and a reference image as inputs, FreeLighting can transfer both lighting and background contents from the reference image to the original image. Different from existed relighting models which need pure scene images with perspective angle alignment as reference, FreeLighting can take images with foreground and any perspective angle as reference. -->

FreeLighting is a DIT-based relighting model designed to manipulate the illumination and background of images. It currently includes two types of models: a text-guided relighting model and an image-guided relighting model.

With the text-guided relighting model, FreeLighting allows users to upload an image and then relight the foreground object while simultaneously replacing the background based on a text prompt. Compared to existing relighting models, FreeLighting excels at preserving the texture and intrinsic properties of the original images.

Regarding the image-guided relighting model, by inputting an original image along with a reference image, FreeLighting can transfer both the lighting and background elements from the reference image to the original image. Unlike other relighting models that require reference images of pure scenes with aligned perspective angles, FreeLighting supports references that include foreground elements and can be taken from any perspective angle. This flexibility makes it more versatile for a wider range of applications. Currently, the image-guided FreeLighting model shows superior performance on portrait photos. The next step is to extend its capabilities to cover more categories. By doing so, FreeLighting aims to offer consistent and high-quality relighting adjustments for diverse subjects and scenes, making it a more comprehensive tool for image manipulation.

We will push the experience demo on Huggingface Space and Modelscope. We will further publish our professional model on our own Software as a Service <a href="https://marketing.k-fashionshop.com/" target="_blank">(SAAS)</a> platform. 👋 Join our <a href="WECHAT.md" target="_blank">WeChat</a> 


<!-- <div align="center"> -->
<!-- We have released our model on <a href="https://huggingface.co/spaces/lllyasviel/LuminaBrush" target="_blank">Huggingface Space</a> and <a href="https://huggingface.co/spaces/lllyasviel/LuminaBrush" target="_blank">ModelScope</a>. We will release more relighting ability in the repository and further publish our professional model on our <a href="https://marketing.k-fashionshop.com/" target="_blank">SAAS</a>. 👋 Join our <a href="WECHAT.md" target="_blank">WeChat</a>  -->
<!-- </div> -->

# ToDo
  - [x] text-guided relighting
  - [x] image-guided relighting
  - [ ] publish model on Huggingface Space and Modelscope
  - [ ] stronger performance for translucent object
  - [ ] image-guided relighting model expands to more categories
  - [ ] technical report

# Demos
You will get a better result when the uploaded image is uniform white lighting.

## Text-guided Relighting
<img src=demos/text-guided/1.webp />
<img src=demos/text-guided/2.webp />
<img src=demos/text-guided/3.webp />
<img src=demos/text-guided/4.webp />

## Image-guided Relighting
<img src=demos/image-guided/2.jpg />
<img src=demos/image-guided/3.jpg />
<img src=demos/image-guided/4.jpg />
<img src=demos/image-guided/1.jpg />


# bib

    @Misc{FreeLighting2025,
      author = {Yuxuan, Liu and MetaCarbon Teams},
      title  = {FreeLighting2025},
      year   = {2025},
    }

# Work in progress

More information will be added later ...



# Related Work

https://github.com/lllyasviel/IC-Light

https://github.com/lllyasviel/LuminaBrush

