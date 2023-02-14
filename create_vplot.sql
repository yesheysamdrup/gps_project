
-- View: public.vplot

-- DROP VIEW public.vplot;

CREATE OR REPLACE VIEW public.vplot
 AS
 SELECT plot.ethram,
    plot.etosarea,
    plot.eplotid,
    st_asGeoJSON(plota.geom) as GEOSHP
  FROM plot
  JOIN plota ON plot.eplotid::text = plota.plotid::text;

  ALTER TABLE public.vplot
  OWNER TO postgres;

