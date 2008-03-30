/*
 * Site Settings For Site
 *
 * Copyright (c) 2008 Dave Merwin (davemerwin.com)
 *
 */
 $(document).ready(function(){
     $('.rounded a').corner({
            tl: { radius: 5 },
            tr: { radius: 5 },
            bl: { radius: 5 },
            br: { radius: 5 },
            validTags: ['a'],
        });
    $('.close').click(function() {
        $(this).parent.close();
        $(this).parent.('.loginout').toggle();
        return false;
    });
 });