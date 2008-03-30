/*
 * Site Settings For Site
 *
 * Copyright (c) 2008 Dave Merwin (davemerwin.com)
 *
 */
 $(document).ready(function(){
    $('.showhide a').click(function(){
        $('#meta').slideToggle('fast');
        $('.showhide a').toggle();
        return false;
    });
 });