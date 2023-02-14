-- View: public.vthram

-- DROP VIEW public.vthram;

CREATE OR REPLACE VIEW public.vthram
 AS
 SELECT district.adescr,
    block.bdescr,
    thram.cthram,
    thram.cownid,
    thram.cownname,
    thram.cdzownname,
    owntype.otdescr,
    thram.cvillage,
    plot.eplotid,
    plot.eplotname,
    plot.etosarea,
    landtype.fdescr,
	vplot.geoshps
   FROM block
     JOIN thram ON block.bgewog = thram.cgewog
     JOIN plot ON thram.cthram = plot.ethram AND thram.cgewog = plot.egewog
     JOIN vplot on plot.eplotid= vplot.eplotid
	 JOIN landtype ON plot.elandtype = landtype.flandtype
     JOIN owntype ON thram.cowntype = owntype.otcode
     JOIN district ON district.adzongkhag = block.bdzongkhag;

ALTER TABLE public.vthram
    OWNER TO postgres;

