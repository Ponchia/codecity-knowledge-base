# Implementation Index

> Catalog of implementations (seeded from CC015 and enriched by later processed sources).

---

## Catalog

| ID | Tool | Year | Status |
|----|------|------|--------|
| I001 | [[software-world]] | 2000 | historical |
| I002 | [[component-city]] | 2002 | historical |
| I003 | [[codecity]] | 2007 | historical |
| I004 | [[vizz3d]] | 2007 | historical |
| I005 | [[skyscrapar]] | 2012 | research |
| I006 | [[uml-city]] | 2007 | research |
| I007 | [[vizzaspectj-3d]] | 2011 | research |
| I008 | [[evostreets]] | 2010 | research |
| I009 | [[explorviz]] | 2013 | research |
| I010 | [[cityvr]] | 2017 | research |
| I011 | [[vr-city]] | 2017 | research |
| I012 | [[code-park]] | 2017 | research |
| I013 | [[high-rise]] | 2017 | research |
| I014 | [[ld-city]] | 2017 | research |
| I015 | [[codecharta]] | 2017 | active |
| I016 | [[code2city]] | 2019 | research |
| I017 | [[code2cityvr]] | 2019 | research |
| I018 | [[jscity]] | 2017 | research |
| I019 | [[softvis3d]] | 2015 | maintained |
| I020 | [[softviz3d]] | 2015 | archived |
| I021 | [[m3tricity]] | 2020 | research |
| I022 | [[langelier-quality-framework]] | 2005 | research |
| I023 | [[gocity]] | 2019 | research |
| I024 | [[codemetropolis]] | 2013 | maintained |
| I025 | [[seccityvr]] | 2025 | research |
| I026 | [[babiaxr-codecity]] | 2021 | research |
| I027 | [[getaviz]] | 2017 | maintained |
| I028 | [[dynacity]] | 2022 | research |
| I029 | [[code-arcades]] | 2025 | research |
| I030 | [[varicity]] | 2021 | research |
| I031 | [[trend-maps]] | 2015 | research |
| I032 | [[imsovision]] | 2001 | historical |
| I033 | [[islandviz]] | 2019 | research |
| I034 | [[codercity]] | 2021 | research |
| I035 | [[city-blocks]] | 2025 | research |
| I036 | [[viseagull]] | 2021 | research |
| I037 | [[codevestimenta]] | 2025 | research |
| I038 | [[crococosmos]] | 2012 | research |

---

## Comparison Matrix

From CC015 Table 1:

| Tool | Language | VR | Building | Src | Static | Dynamic | Instr |
|------|----------|-----|----------|-----|--------|---------|-------|
| Software World | Java | Maverik | function | n/a | LOC; #methods; public/private; #parameters; param. types | n/a | n/a |
| Component City | XML | VRML | compon. | n/a | func. attrib.; #methods | n/a | n/a |
| CodeCity | SmallTalk, Java, C++ | n/a | class | n/a | #attributes; #methods; package struct. | n/a | n/a |
| Vizz3D | C/C++ | n/a | function | n/a | LOC; complexity; call graphs; contains; inheritance; str. conn. comp. | gprof | none (-pg) |
| SkyscrapAR | Java | AR | class | n/a | churn | n/a | n/a |
| UML-City | UML | n/a | class / various | n/a | various metrics; author | n/a | n/a |
| VizzAspectJ-3D | Java, AspectJ | n/a | class / aspect | n/a | #methods; #pointcuts; #advices | n/a | n/a |
| EvoStreets | Java | n/a | class | n/a | module age; coupling; #dependencies; module size; last mod. date; author; inheritance | n/a | n/a |
| SynchroVis / ExplorViz | Java | Rift | class | n/a | implementation; association; LOC | instances; calls; thread op | Kieker traces |
| CityVR | Java/C++ | Vive | class | yes | LOC; #methods; #attributes | n/a | n/a |
| VR City | Java | Vive | class | yes | LOC; #methods; coupling; author | trace loc. | inTrace traces |
| Code Park | C# | n/a | class | yes | size; method names | n/a | n/a |
| High-Rise | Java | n/a | function | no | n/a | time | ASM injection |
| LD-City | LD-R | n/a | (dynamic) | n/a | #instances; #properties | n/a | n/a |

---

## Statistics

- **Total implementations**: 38
- **Last updated**: 2026-01-05
- **Sources processed**: CC009, CC014, CC015, CC017, CC018, CC020, CC023, CC024, CC025, CC035, CC036, CC038, CC040, CC041, CC043, CC053, CC059, CC075, CC079, CC080, CC085, CC086, CC091, CC092, CC093, CC094, CC096, CC102, CC103, CC104, CC106, CC069, CC071, CC077, CC098, CC108, CC116, CC117, CC128, CC129, CC130, CC131, CC133, CC134, CC137, CC140, CC002, CC005, CC006, CC021, CC026, CC030, CC034, CC045, CC054, CC055, CC057, CC064, CC066, CC070, CC074, CC076, CC078, CC083, CC084, CC100, CC101, CC107, CC114, CC120, CC121, CC126, CC136, CC143, CC147, CC148
