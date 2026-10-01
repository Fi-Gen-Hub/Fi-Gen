# -*- coding: utf-8 -*-
PAGES = {}

PAGES['air-freight'] = dict(
  name='Air Freight', icon='fa-plane-departure',
  meta_description='Fi-Gen Logistics air freight services &mdash; express, standard and charter air cargo with door-to-door delivery, real-time tracking and dangerous goods handling worldwide.',
  keywords='air freight, express air cargo, charter flights, door to door air delivery, import export by air',
  hero_image='https://images.unsplash.com/photo-1540962351504-03ddf9abac6a?q=80&w=2070&auto=format&fit=crop',
  cta_image='https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=2000&auto=format&fit=crop',
  hero_title='Fast &amp; Secure <span class="gradient-text">Air Freight</span> Solutions',
  hero_sub='Time-critical shipments delivered via a global network of airline partnerships. Express, standard and charter options — backed by 25+ years of professional expertise and 24/7 support.',
  chips=[('fa-bolt','Express in 24–72 hrs'),('fa-globe','50+ destinations'),('fa-box-open','DGR certified'),('fa-headset','24/7 support')],
  overview_title='Why Ship Air with Fi-Gen?',
  overview_paras=[
    'When speed matters most, Fi-Gen&rsquo;s <strong>air freight division</strong> moves your cargo on the fastest lanes between India, the UK, Europe, North America, the Gulf and Asia-Pacific. Our long-standing allocations with leading carriers mean we secure space even during peak season.',
    'From a single urgent sample parcel to full charter movements, we manage every step: pickup, export documentation, air waybill issuance, customs clearance at both ends, and final door delivery — one accountable partner, zero hand-off gaps.',
    'Every booking is handled by a dedicated air cargo specialist who monitors your shipment milestone-by-milestone and proactively resolves issues before they become delays.'
  ],
  features=['Door-to-door and airport-to-airport options','Consolidation (groupage) for small high-value shipments','Full charters &amp; next-flight-out express services','IATA/DGR-compliant dangerous goods handling','Temperature-controlled ULDs for pharma &amp; perishables','Real-time airway-bill tracking and milestone alerts'],
  info_rows=[('Transit time','24 – 96 hours'),('Coverage','50+ countries'),('Cargo types','General, DG, Pharma, Perishable'),('Tracking','Live AWB updates'),('Support','24/7 dedicated desk')],
  capabilities_title='Complete <span class="gradient-text">Air Cargo</span> Capabilities',
  capabilities_sub='Whatever flies, we move it — safely, compliantly and on schedule.',
  overview_cards=[
    dict(icon='fa-bolt', title='Express Air Freight', text='Next-flight-out and priority handling for critical parts, documents and emergency consignments.'),
    dict(icon='fa-layer-group', title='Air Consolidation', text='Cost-effective groupage for shipments from 45 kg upward — pay only for the space you use.'),
    dict(icon='fa-chart-line', title='Charter Services', text='Full and part charters for project cargo, oversized freight and disaster-relief movements.'),
    dict(icon='fa-pills', title='Pharma &amp; Cold Chain', text='GDP-compliant temperature-managed air logistics with validated cool containers and data loggers.'),
    dict(icon='fa-flask', title='Dangerous Goods', text='IATA DGR-certified documentation, labelling and handling for batteries, chemicals and more.'),
    dict(icon='fa-file-signature', title='Doorstep Customs', text='Export and import clearance bundled into one seamless air freight solution.')],
  process_sub='Five simple steps from enquiry to delivery — we handle the complexity.',
  steps=[
    dict(title='Share Your Requirements', text='Origin, destination, commodity, weight/volume and required delivery date. Quotation within 2 hours.'),
    dict(title='Route &amp; Carrier Selection', text='We compare direct and connecting options across our airline network to balance speed and cost.'),
    dict(title='Pickup &amp; Export Handling', text='Collection, warehousing, build-up, AWB issuance and export customs filing are managed end-to-end.'),
    dict(title='In-Flight Visibility', text='Track your AWB live; our desk monitors departures, transits and arrivals around the clock.'),
    dict(title='Clearance &amp; Final Delivery', text='Import clearance, breakdown and last-mile delivery to the consignee&rsquo;s door, with POD confirmation.')],
  stats=[dict(target=15000, desc='Shipments Delivered'), dict(target=50, desc='Countries Served'), dict(target=98, desc='% On-Time Departure'), dict(target=24, desc='/7 Expert Desk')],
  faqs=[
    dict(q='How fast can my cargo reach its destination by air?', a='Most international air shipments are delivered within 24–96 hours door-to-door depending on the lane, customs and whether express or consolidation service is used.'),
    dict(q='Can you handle dangerous goods by air?', a='Yes. Our team is IATA DGR trained and handles Class 3, 8, 9 (including lithium batteries) and other regulated cargo with complete documentation and compliant packaging guidance.'),
    dict(q='Do you provide door-to-door service including customs?', a='Absolutely. We quote both airport-to-airport and fully inclusive door-to-door services with export and import customs clearance included.'),
    dict(q='What documents do I need for an air export?', a='Typically a commercial invoice, packing list, shipping instructions and any permits specific to the commodity (e.g., FDA, TADA, DGFT). Our team will confirm exact requirements for your lane.'),
    dict(q='Is insurance available for air cargo?', a='Yes — all-risk air cargo cover can be arranged at quotation time; see our Cargo Insurance service for details.')],
  cta_text='Get a competitive air freight quote within 2 hours — with clearance, tracking and 24/7 support built in.'
)

PAGES['sea-freight'] = dict(
  name='Sea Freight', icon='fa-ship',
  meta_description='Fi-Gen Logistics ocean freight services — FCL, LCL, reefer and project cargo across major global trade lanes with door-to-door delivery and customs clearance.',
  keywords='sea freight, ocean freight, FCL, LCL, container shipping, reefer cargo, port to port, door to door',
  hero_image='https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?q=80&w=2070&auto=format&fit=crop',
  cta_image='https://images.unsplash.com/photo-1605745341112-85968b19335b?q=80&w=2000&auto=format&fit=crop',
  hero_title='Reliable <span class="gradient-text">Ocean Freight</span> Across Every Trade Lane',
  hero_sub='FCL and LCL solutions across major global routes — cost-effective for bulk and heavy cargo, with reefer, OOG and project expertise behind every booking.',
  chips=[('fa-container-storage','FCL &amp; LCL'),('fa-snowflake','Reefer &amp; OOG'),('fa-route','All major lanes'),('fa-anchor','25+ yrs experience')],
  overview_title='Sea Freight That Works for Your Margins',
  overview_paras=[
    'Ocean shipping carries over 80% of global trade — and choosing the right partner makes the difference between predictable landed costs and unpleasant surprises. Fi-Gen negotiates <strong>contracted rates with major liners</strong> and selects the routing that balances transit time, reliability and price.',
    'Whether you need a full container, shared LCL space, a refrigerated unit or break-bulk for out-of-gauge machinery, our team manages everything: booking, container loading, VGM, bill of lading, port formalities, insurance and destination delivery.',
    'With established corridors between India, the UK, Europe, the Americas, Middle East and Asia, plus trusted overseas agents, your cargo gets a single point of accountability from shipper&rsquo;s door to consignee&rsquo;s door.'
  ],
  features=['FCL (20&rsquo;, 40&rsquo;, 40&rsquo;HC) with contracted liner rates','LCL consolidation for shipments from 1 CBM','Reefer containers with remote temperature monitoring','Out-of-gauge, break-bulk &amp; project cargo planning','Port-to-port, door-to-door &amp; EXW/CIF/DDP terms','Bill of lading, manifest &amp; LC documentation support'],
  info_rows=[('Transit time','12 – 35 days by route'),('Options','FCL · LCL · Reefer · OOG'),('Incoterms','EXW / FOB / CIF / DDP'),('Tracking','Container &amp; vessel ETA'),('Support','24/7 ops desk')],
  capabilities_title='Our <span class="gradient-text">Ocean</span> Service Range',
  capabilities_sub='One partner for every container, every cargo type, every port.',
  overview_cards=[
    dict(icon='fa-container-storage', title='Full Container Loads', text='Committed space and competitive contracts on all mainliner loops, including peak-season protection.'),
    dict(icon='fa-cubes', title='LCL Groupage', text='Weekly consolidations on high-frequency lanes — share the container, cut the cost.'),
    dict(icon='fa-snowflake', title='Reefer Shipping', text='Frozen and chilled cargo with pre-trip inspections, set-point control and telemetry.'),
    dict(icon='fa-crane', title='Project &amp; OOG Cargo', text='Engineering surveys, route studies, special stows and heavy-lift coordination for oversized cargo.'),
    dict(icon='fa-people-arrows', title='NVOCS &amp; Buyer&rsquo;s Console', text='Freight booked in your favour with independent invoicing and transparent surcharges.'),
    dict(icon='fa-file-invoice-dollar', title='Documentation &amp; LC', text='BL amendments, telex releases, letters of credit and port paperwork handled precisely.')],
  process_sub='From enquiry to discharge — a transparent, milestone-driven workflow.',
  steps=[
    dict(title='Enquiry &amp; Routing Plan', text='Tell us cargo dimensions, Incoterms and timeline; we propose optimal load type, liner and transit.'),
    dict(title='Booking &amp; Container Supply', text='Space confirmed with the carrier; empty containers delivered for stuffing at your site or our warehouse.'),
    dict(title='Stuffing, VGM &amp; Export Formalities', text='Loading supervision, VGM weighing, custom sealing, SI submission and export clearance.'),
    dict(title='Ocean Transit &amp; Monitoring', text='Live vessel tracking, ETA updates and proactive communication on any disruptions.'),
    dict(title='Discharge &amp; Door Delivery', text='Import clearance support, devanning if required, and delivery to final destination with proof of delivery.')],
  stats=[dict(target=50, desc='Global Ports'), dict(target=12000, desc='Containers Moved'), dict(target=25, desc='Years Experience'), dict(target=100, desc='% Documentation Accuracy')],
  faqs=[
    dict(q='What is the difference between FCL and LCL?', a='FCL means your cargo books an entire container exclusively; LCL means your goods share a container and you pay per cubic metre. LCL suits smaller shipments, FCL is usually faster and cheaper per unit above ~14 CBM.'),
    dict(q='Which Incoterms do you support?', a='We regularly quote and execute EXW, FOB, CFR, CIF and fully delivered DDP shipments, handling every obligation in between.'),
    dict(q='Can you ship temperature-sensitive products by sea?', a='Yes — reefer containers from -25°C to +25°C with continuous monitoring, pre-trip inspection reports and optional telemetry during transit.'),
    dict(q='How is my cargo protected against damage?', a='Proper dunnage and bracing, sealed containers, careful stevedore coordination, and optional all-risk marine cargo insurance which we can arrange in minutes.'),
    dict(q='Who handles customs at the destination port?', a='Our own team and vetted agent network manage destination clearance so you deal with one partner from origin to final delivery.')],
  cta_text='Compare FCL/LCL rates for your lane today — quotes include surcharges, docs and clearance options with no hidden fees.'
)

PAGES['customs-clearance'] = dict(
  name='Customs Clearance', icon='fa-file-invoice',
  meta_description='Expert customs brokerage for import and export clearance — HS classification, duty advisory, DGFT compliance and licensing with a zero-error record by Fi-Gen Logistics.',
  keywords='customs clearance, customs broker, HS code, import clearance, export clearance, DGFT, ICEGATE, duty calculation',
  hero_image='https://images.unsplash.com/photo-1554734816-68cdf6c4f5b6?q=80&w=2070&auto=format&fit=crop',
  cta_image='https://images.unsplash.com/photo-1450101499163-c8848c66ca85?q=80&w=2000&auto=format&fit=crop',
  hero_title='Customs Clearance Done <span class="gradient-text">Right. First Time.</span>',
  hero_sub='Licensed brokerage for imports and exports across Indian ports, airports and ICDs — with UK/EU entry support through our partner network. Complex regulations, simplified.',
  chips=[('fa-stamp','Licensed broker'),('fa-search-dollar','HS classification'),('fa-file-contract','DGFT &amp; licences'),('fa-check-double','Zero-error record')],
  overview_title='Your Compliance Shield at Every Border',
  overview_paras=[
    'Customs is where good logistics plans succeed or fail. A single misclassified HS code or missing licence can turn a routine shipment into weeks of demurrage. Fi-Gen&rsquo;s in-house brokers file thousands of declarations annually with a <strong>zero-error track record</strong> built over 25 years.',
    'We handle complete import and export documentation — bills of entry and shipping bills, IGST/duty computation, valuation, examinations and approvals — through ICEGATE and at the port counter, coordinating directly with officers, surveyors and terminal operators.',
    'Beyond clearance, we act as your trade-compliance advisor: duty-optimisation under relevant schemes, EPCG and Advance Authorisation guidance, and audit-ready records so your business stays clean with regulators.'
  ],
  features=['Import &amp; export declaration filing (ICEGATE)','HS code classification &amp; duty/tariff advisory','DGFT licences, authorisations &amp; RoDTEP claims','Valuation, exemptions &amp; benefit scheme application','Examination, assessment &amp; release coordination','KYC, IEC registration &amp; compliance audits'],
  info_rows=[('Ports covered','All major India ports/ICDs'),('Turnaround','Same-day filing typical'),('Advisory','HS · Duty · Schemes'),('Accuracy','Zero-error record'),('Support','24/7 declarations desk')],
  capabilities_title='Full-Spectrum <span class="gradient-text">Trade Compliance</span>',
  capabilities_sub='Everything between your paperwork and your cargo release.',
  overview_cards=[
    dict(icon='fa-file-import', title='Import Clearance', text='BOE preparation, B/E amendments, provisional assessments, anti-profiteering replies and speedy release.'),
    dict(icon='fa-file-export', title='Export Clearance', text='Shipping bills, incentives (RoDTEP/Drawback), e-invoices, LOI extensions and exporter documentation.'),
    dict(icon='fa-barcode', title='HS Classification', text='Binding-precedent research and defensible classification to keep duty exposure legal and minimal.'),
    dict(icon='fa-scale-balanced', title='Duty Advisory', text='Scheme selection, FTA/CEPA origin strategy and total landed-cost modelling before you ship.'),
    dict(icon='fa-id-card', title='Licences &amp; Registrations', text='IEC, DGFT authorisations, AD code, GST and departmental NOCs obtained and maintained.'),
    dict(icon='fa-magnifying-glass-chart', title='Audit &amp; Training', text='Periodic compliance audits and team training so issues never repeat.')],
  process_sub='A disciplined five-stage method behind every clean clearance.',
  steps=[
    dict(title='Pre-Arrival Review', text='We study invoices, packing lists and prior rulings to pre-classify goods and flag permit requirements early.'),
    dict(title='Documentation Build', text='Declarations drafted with correct valuation, origin and scheme benefits — checked by a senior broker before filing.'),
    dict(title='Filing &amp; Assessment', text='Electronic filing via ICEGATE, duty payment, and coordination through assessment and examination if selected.'),
    dict(title='Release &amp; Delivery', text='Out-of-charge obtained, delivery order processed and cargo handed to the nominated transporter.'),
    dict(title='Post-Clearance Audit', text='Every file archived and reviewed; incentive claims tracked to realisation with monthly compliance reports.')],
  stats=[dict(target=20000, desc='Declarations Filed'), dict(target=25, desc='Years Brokerage'), dict(target=100, desc='% Compliance Rate'), dict(target=2, desc='Hr Avg. Response')],
  faqs=[
    dict(q='Do I need an Importer Exporter Code (IEC)?', a='Yes, an IEC from DGFT is mandatory for cross-border trade in India. We help you obtain it along with AD code registration and GST linkage.'),
    dict(q='How long does customs clearance take?', a='Most compliant consignments clear within 24–48 hours of arrival. Problematic files (permits, valuation disputes) are resolved faster when a broker is engaged pre-arrival — as we recommend.'),
    dict(q='Can you reduce my duty liability legally?', a='Often yes — through correct HS classification, applicable exemptions, FTAs/CEPTA origin claims and schemes like Advance Authorisation or EPCG. We only ever advise lawful optimisation.'),
    dict(q='Do you handle UK and EU customs as well?', a='Yes. For UK/EU movements we work with licensed customs partners to ensure CDS/ENS entries and post-Brexit requirements are met smoothly.'),
    dict(q='What happens if my goods are detained?', a='Our brokers attend examinations personally, file representations, and coordinate with appraisers and departmental heads to secure release with minimum demurrage.')],
  cta_text='Send us your documents for a free pre-clearance check — we&rsquo;ll flag risks and estimate your exact duty before cargo moves.'
)

PAGES['warehousing'] = dict(
  name='Warehousing &amp; Distribution', icon='fa-warehouse',
  meta_description='Bonded and non-bonded warehousing, inventory management, pick-pack fulfilment and last-mile distribution by Fi-Gen Logistics — including e-commerce ready fulfilment.',
  keywords='warehousing, bonded warehouse, distribution, pick and pack, inventory management, fulfilment, last mile delivery',
  hero_image='https://images.unsplash.com/photo-1553413077-190dd30588be?q=80&w=2070&auto=format&fit=crop',
  cta_image='https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=2000&auto=format&fit=crop',
  hero_title='Smart <span class="gradient-text">Warehousing</span> &amp; Distribution',
  hero_sub='Strategically located bonded and non-bonded facilities with WMS-driven inventory control, pick-pack fulfilment and fast distribution — the backbone of your supply chain.',
  chips=[('fa-shield-halved','Bonded storage'),('fa-bars-progress','Live WMS'),('fa-boxes-stacked','Pick &amp; Pack'),('fa-truck-fast','Last-mile')],
  overview_title='Storage That Adds Value, Not Cost',
  overview_paras=[
    'Inventory sitting idle is capital locked away. Fi-Gen&rsquo;s warehouses combine <strong>bonded and domestic storage</strong> with an integrated Warehouse Management System so you always know exactly what you own, where it is, and what it costs you.',
    'Our facilities support import consolidation, deconsolidation, breaking bulk, kitting, labelling, quality checks and immediate onward distribution — turning a static store into an active value-add centre.',
    'For e-commerce sellers we run same-day pick-pack-and-ship operations with returns processing, so your warehouse scales automatically with your festive-season spikes.'
  ],
  features=['Bonded &amp; non-bonded racking and floor storage','WMS with barcode scanning and live client portal','Pick, pack, label, kit &amp; value-added services','Import consolidation / export groupage bays','Temperature-aware zones for sensitive goods','Inventory reporting, cycle counts &amp; insurance cover'],
  info_rows=[('Facilities','Trichy + partner hubs'),('Systems','Barcode WMS + portal'),('Flexibility','Short &amp; long term'),('Add-ons','Kitting · Labelling'),('Access','24/7 security monitored')],
  capabilities_title='End-to-End <span class="gradient-text">Distribution</span> Services',
  capabilities_sub='From bulk inbound to parcel outbound — one integrated operation.',
  overview_cards=[
    dict(icon='fa-warehouse', title='Bonded Warehousing', text='Store dutiable goods duty-unpaid until you need them; ideal for JIT manufacturing and re-export trade.'),
    dict(icon='fa-list-check', title='Inventory Control', text='Real-time stock levels, batch/expiry tracking, reorder alerts and monthly reconciliation reports.'),
    dict(icon='fa-hand', title='Fulfilment &amp; Pick-Pack', text='Order-level picking with scan verification, branded packing and same-day handover to courier partners.'),
    dict(icon='fa-code-branch', title='Kitting &amp; Co-Packing', text='Assembly, bundling, promotional kits and repackaging executed to your SOPs.'),
    dict(icon='fa-truck-fast', title='Distribution Network', text='FTL/LTL dispatch and last-mile parcels across Tamil Nadu and all-pincode India-wide coverage.'),
    dict(icon='fa-rotate-left', title='Returns Management', text='Reverse logistics, inspection, refurbishment decisions and restocking without the headaches.')],
  process_sub='How goods flow through a Fi-Gen facility.',
  steps=[
    dict(title='Inbound Receipt', text='Goods received against ASN, counted, scanned and quality-checked; discrepancies flagged within hours.'),
    dict(title='Put-Away &amp; Storage', text='Systematic slotting by velocity and handling needs, in bonded or domestic zones as required.'),
    dict(title='Order Processing', text='Orders flow in via portal/email/API; waves are picked, packed and verified by barcode scan.'),
    dict(title='Dispatch', text='Carrier assignment based on cost/speed, manifests generated, and shipments released with tracking.'),
    dict(title='Reporting', text='Daily dashboards on stock movement, fill-rate, ageing and charges — full transparency, no surprises.')],
  stats=[dict(target=100000, desc='Sq Ft Managed'), dict(target=99, desc='% Inventory Accuracy'), dict(target=300, desc='Orders/Day Capacity'), dict(target=24, desc='/7 Gate Security')],
  faqs=[
    dict(q='What is bonded warehousing and do I need it?', a='Bonded warehouses hold imported goods before duty is paid. You save cash-flow by clearing (and paying duty on) only what you remove for sale or production.'),
    dict(q='Can you integrate with my sales channels?', a='Yes. Our WMS connects with major marketplaces and Shopify-based storefronts for automatic order sync — see our E-commerce Logistics service.'),
    dict(q='How is my stock insured and secured?', a='Facilities are CCTV-monitored with 24/7 security, and storage can be covered under comprehensive stock insurance policies on request.'),
    dict(q='What are your charging models?', a='Flexible: per-pallet/per-sq-ft monthly storage plus transactional handling fees, or bespoke contracts for dedicated operations.'),
    dict(q='Can you handle seasonal volume spikes?', a='That&rsquo;s exactly why clients choose us — labour, packing stations and carrier capacity are scaled ahead of your forecast peaks.')],
  cta_text='Book a facility walkthrough or request a storage + fulfilment proposal tailored to your SKU profile.'
)

PAGES['road-rail-freight'] = dict(
  name='Road &amp; Rail Freight', icon='fa-truck-moving',
  meta_description='Domestic and cross-border road and rail freight — FTL, LTL, temperature-controlled and GPS-tracked fleet services by Fi-Gen Logistics.',
  keywords='road freight, truck transport, rail freight, FTL, LTL, surface cargo, multi-modal, temperature controlled transport',
  hero_image='https://images.unsplash.com/photo-1519003729863-2021a646513c?q=80&w=2070&auto=format&fit=crop',
  cta_image='https://images.unsplash.com/photo-1492233416424-8a3460582ad2?q=80&w=2000&auto=format&fit=crop',
  hero_title='Ground Movements You Can <span class="gradient-text">Count On</span>',
  hero_sub='Domestic and cross-border road &amp; rail connectivity that links your factory, port and customer — optimised for cost, safety and transit reliability.',
  chips=[('fa-truck','FTL &amp; LTL'),('fa-train','Rail &amp; multi-modal'),('fa-location-dot','GPS tracked'),('fa-temperature-half','Reefer fleet')],
  overview_title='The Backbone of Every Supply Chain',
  overview_paras=[
    'Between the first mile and the last, surface transport decides whether your logistics budget succeeds. Fi-Gen operates a curated fleet network — from 1-tonne temps to 32-foot multi-axle trailers and rail rakes — with drivers, escorts and vetted transporters under fixed contracts.',
    'We design <strong>multi-modal routes</strong> combining road and rail where economics allow, cutting freight cost and carbon while keeping transit times dependable for scheduled deliveries.',
    'Every vehicle runs on GPS with geofencing and ETAs shared to your team automatically, so movement visibility matches what you expect from air and ocean tracking.'
  ],
  features=['Full truck loads (FTL) &amp; part loads (LTL) pan-India','Multi-axle, container chassis &amp; tail-lift vehicles','Temperature-controlled reefers (-25°C to +25°C)','Rail wagon &amp; rake bookings, ICD transfers','Cross-border surface corridors (Nepal, Bangladesh belt)','ETAS/good-loading practices &amp; escort options'],
  info_rows=[('Coverage','Pan-India + corridors'),('Fleet','Temp → 32&rsquo; MAI'),('Tracking','GPS + geofence ETA'),('Options','FTL · LTL · Rail'),('Handling','Tail-lift · Crane')],
  capabilities_title='Surface <span class="gradient-text">Transport</span> Capabilities',
  capabilities_sub='Right equipment, right route, right price — every time.',
  overview_cards=[
    dict(icon='fa-truck', title='Full Truck Load', text='Dedicated vehicles for time-certain, damage-minimised point-to-point movements at volume rates.'),
    dict(icon='fa-truck-arrow-right', title='Part Load / LTL', text='Scheduled consolidations on trunk routes — daily departures between major industrial hubs.'),
    dict(icon='fa-train', title='Rail Freight', text='Terminal-to-terminal and double-stack rail for cost-efficient long-haul bulk cargo.'),
    dict(icon='fa-temperature-half', title='Cold Chain Road', text='Reefer vans with digital temperature logging for food, floral, dairy and pharma distribution.'),
    dict(icon='fa-road', title='Project Movement', text='Permit management, route surveys and escorting for oversize/weight consignment by road.'),
    dict(icon='fa-exchange-alt', title='Port &amp; ICD Drayage', text='Container shunting between ports, CFS and ICDs tightly synchronised with vessel and rail schedules.')],
  process_sub='Simple briefing in — measurable execution out.',
  steps=[
    dict(title='Load Briefing', text='Weight, dimensions, pickup/drop addresses and service level define the equipment spec we source.'),
    dict(title='Vehicle Assignment', text='Contracted vehicle allocated with driver KYC, insurance and fitness documents verified.'),
    dict(title='Loading &amp; Seal', text='Supervised loading, lashing per standards, seal numbers recorded and shared before departure.'),
    dict(title='Transit Monitoring', text='GPS milestones, geofenced ETA updates and exception alerts pushed to stakeholders.'),
    dict(title='Proof of Delivery', text='Signed POD, photographs and unload report uploaded to your portal within hours of delivery.')],
  stats=[dict(target=500, desc='Vetted Vehicles'), dict(target=5000, desc='Deliveries/Month'), dict(target=15, desc='States Covered Daily'), dict(target=99, desc='% Damage-Free')],
  faqs=[
    dict(q='How quickly can a truck be arranged?', a='On trunk routes typically same-day or next-morning placement; dedicated contract fleets guarantee tighter windows for regular lanes.'),
    dict(q='Is my cargo insured during road transit?', a='Vehicles carry transit insurance; we additionally recommend and arrange all-risk cargo cover for high-value loads — see Cargo Insurance.'),
    dict(q='Can you do temperature-controlled distribution?', a='Yes, reefer fleet from -25°C to +25°C with continuous data logging shared with every consignment.'),
    dict(q='Do you handle intermodal road+rail shipments?', a='Absolutely — we design road-rail combinations for long distances, managing drayage at both terminals as one booking.'),
    dict(q='What about interstate permits and check-posts?', a='Our transport desk manages permits, octroi/LBS equivalents and check-post queues so drivers keep moving.')],
  cta_text='Tell us the lane and the load — receive a firm surface freight rate with GPS visibility in under 2 hours.'
)

PAGES['cargo-insurance'] = dict(
  name='Cargo Insurance &amp; Risk', icon='fa-shield-alt',
  meta_description='Marine and air cargo insurance with all-risk cover, fast claims settlement and risk engineering by Fi-Gen Logistics — protecting every shipment door to door.',
  keywords='cargo insurance, marine insurance, all risk cover, transit insurance, claims settlement, risk management',
  hero_image='https://images.unsplash.com/photo-1560472354-b33ff0c44a43?q=80&w=2070&auto=format&fit=crop',
  cta_image='https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=2000&auto=format&fit=crop',
  hero_title='Protect Every Rupee of <span class="gradient-text">Your Cargo</span>',
  hero_sub='Comprehensive marine, air and land cargo insurance with proactive risk engineering and claims advocacy — because one uninsured incident can erase a year of profit.',
  chips=[('fa-umbrella','All-risk cover'),('fa-gavel','Claims advocacy'),('fa-percent','Competitive premiums'),('fa-file-shield','Annual policies')],
  overview_title='Risk Managed Before It Happens',
  overview_paras=[
    'Freight moves through countless hands — trucks, terminals, vessels, cranes, warehouses. Each transfer adds exposure to damage, theft, shortage and natural calamity. Fi-Gen&rsquo;s insurance desk places your cargo with <strong>leading underwriters</strong> at institutional rates, on terms that actually pay when it matters.',
    'We assess your commodity, packaging and route to recommend the right clause structure — Institute Cargo Clauses (A) all-risk, named perils, warehouse-to-warehouse extension, and add-ons like strikes, war and rejections cover.',
    'If the worst happens, we don&rsquo;t just pass you a phone number: our team files the claim, appoints surveyors, compiles evidence and negotiates settlement on your behalf until funds realise.'
  ],
  features=['Marine, air, land &amp; courier parcel cover','Institute Cargo Clauses (A) all-risk placement','Warehouse-to-warehouse &amp; stock throughput policies','Add-ons: war, strikes, rejection, delay in start','Loss-of-profit and consequential cover options','End-to-end claims filing and settlement support'],
  info_rows=[('Cover basis','CIF +10% or agreed value'),('Underwriters','Top-rated insurers'),('Response','Quote within 2 hours'),('Claims','Handled by our desk'),('Plans','Per-shipment or annual')],
  capabilities_title='Beyond the Policy: <span class="gradient-text">Risk Engineering</span>',
  capabilities_sub='Prevention first — indemnity second.',
  overview_cards=[
    dict(icon='fa-magnifying-glass', title='Route Risk Audit', text='Lane-by-lane loss history analysis to set deductibles, clauses and precautions sensibly.'),
    dict(icon='fa-box-circle-check', title='Packaging Reviews', text='Simple packaging upgrades that prevent the majority of damage claims — we brief your team.'),
    dict(icon='fa-file-signature', title='Policy Structuring', text='Open/annual policies for regular shippers: one premium, automatic cover, quarterly declarations.'),
    dict(icon='fa-person-running', title='Emergency Funding', text='Salvage, separation and particular-average guidance so a casualty doesn&rsquo;t freeze your cash.'),
    dict(icon='fa-comments', title='Claims Advocacy', text='Surveyor coordination, documentation packs and insurer negotiation handled start to finish.'),
    dict(icon='fa-chart-simple', title='Loss Analytics', text='Annual claims dashboards revealing patterns — so losses shrink year over year.')],
  process_sub='How we insure and defend your cargo.',
  steps=[
    dict(title='Declare the Shipment', text='Share invoice value, mode, packing and route — we advise the optimal clause structure instantly.'),
    dict(title='Quotation &amp; Binding', text='Best terms from panel underwriters; cover bound online with policy/certificate issued same day.'),
    dict(title='Prevention Guidance', text='You receive packing and handling checklists specific to your commodity and lane.'),
    dict(title='Incident Response', text='If loss occurs: notify us immediately — we initiate survey, mitigate further damage and preserve rights.'),
    dict(title='Claim &amp; Settlement', text='Complete claim file submitted; we chase, negotiate and follow through until settlement lands.')],
  stats=[dict(target=500, desc='Claims Resolved'), dict(target=96, desc='% Settlement Success'), dict(target=7, desc='Days Avg. Settlement'), dict(target=24, desc='/7 Claims Hotline')],
  faqs=[
    dict(q='Is carrier liability enough instead of insurance?', a='No. Carrier liability is capped by convention (often a few dollars per kg) and excludes many causes. All-risk cargo insurance covers the true value of goods from warehouse to warehouse.'),
    dict(q='When should I buy — before or after shipment?', a='Before the journey begins. Cover cannot be backdated once cargo has moved or an incident occurred; include insurance at quotation stage as standard practice.'),
    dict(q='What is an open/annual cargo policy?', a='One policy covering all your shipments in a year at negotiated rates — premium settled quarterly on declared values. Cheaper and administratively effortless for regular exporters.'),
    dict(q='How fast are claims settled?', a='With our documentation-first approach, straightforward claims typically settle within 7–15 days of survey completion.'),
    dict(q='Do you insure high-value goods like jewellery and electronics?', a='Yes — including specified-peril and guarded-transit structures for gems, bullion and high-theft-risk electronics.')],
  cta_text='Insure your next consignment in minutes — send the invoice and we&rsquo;ll return best-cover options before cargo rolls.'
)

PAGES['ecommerce'] = dict(
  name='E-commerce Logistics', icon='fa-shopping-cart',
  meta_description='Amazon &amp; Shopify e-commerce fulfilment for UK and India sellers — 7 years of proven experience, FBA prep, multichannel warehousing, successful project handover and 24/7 profitable growth support by Fi-Gen.',
  keywords='ecommerce logistics, amazon fba, shopify fulfillment, uk india ecommerce, fba prep, multichannel fulfillment, seller support',
  hero_image='https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=2070&auto=format&fit=crop',
  cta_image='https://images.unsplash.com/photo-1523206489231-c36d43c79e73?q=80&w=2000&auto=format&fit=crop',
  hero_title='E-commerce Fulfilment for <span class="gradient-text">Amazon &amp; Shopify</span> Sellers',
  hero_sub='UK- and India-based e-commerce support backed by <strong>7 years of field experience</strong> — successful project launches, smooth handovers, 24/7 support and profitable operations you can scale.',
  chips=[('fa-amazon','Amazon FBA &amp; FBM'),('fa-shopify','Shopify fulfilment'),('fa-flag-gb','UK operations'),('fa-globe-asia','India operations'),('fa-clock','24/7 support'),('fa-trophy','7 years proven')],
  overview_title='7 Years Turning Stores Into Profitable Brands',
  overview_paras=[
    'Selling online is easy. Running a <strong>profitable</strong> e-commerce operation is not. For the past 7 years, Fi-Gen has successfully launched, operated and handed over Amazon and Shopify businesses for sellers in the UK and India — managing sourcing, listings, pricing, advertising, fulfilment and customer service as one integrated engine.',
    'Our UK-based and India-based teams work the local marketplaces natively: Amazon.co.uk, Amazon.in, Amazon.com US expansion, Flipkart, plus Shopify DTC storefronts with payments, tax (VAT/GST) and courier integrations configured correctly from day one.',
    'Every engagement follows a documented playbook, so when we hand the project over, you receive clean SOPs, trained staff, healthy account metrics and a growth roadmap — not a fragile operation that collapses without us.',
    'And after handover, our <strong>24/7 support desk</strong> stays with you: monitoring, restock planning, PPC tuning and issue resolution, keeping your stores profitable round the clock across both time zones.'
  ],
  features=['Amazon Seller Central setup &amp; account health management','FBA inbound planning, prep, labelling &amp; shipment creation','FBM / Seller-Fulfilled Prime with UK &amp; India carrier integrations','Shopify store build, apps, theme &amp; payment configuration','Product research, listing SEO, A+ content &amp; image packs','PPC / advertising management tuned to ACOS targets','UK VAT &amp; India GST compliance for marketplaces','Inventory forecasting and replenishment automation','Customer service desks (email/chat) with prime-level SLAs','Documented SOPs, KPI dashboards &amp; successful project handover','24/7 monitoring and support after go-live','Returns, refunds &amp; chargeback management'],
  info_rows=[('Experience','7 years in e-commerce'),('Marketplaces','Amazon UK · IN · US, Flipkart'),('Platforms','Shopify, WooCommerce'),('Operations','UK &amp; India based teams'),('Handover','100% projects handed over'),('Support','24/7 post-launch')],
  capabilities_title='Full-Stack <span class="gradient-text">Seller Services</span>',
  capabilities_sub='From unboxing a sample to a handed-over seven-figure store.',
  overview_cards=[
    dict(icon='fa-amazon', title='Amazon Operations', text='Account setup, category approvals, listing optimisation, FBA/FBM strategy, Buy Box tactics and account-health defence.'),
    dict(icon='fa-shopify', title='Shopify Store Builds', text='Conversion-focused storefronts with product feeds, subscriptions, upsells, analytics pixels and payment gateways wired in.'),
    dict(icon='fa-box-open', title='FBA Prep &amp; Inbound', text='Receiving, inspection, poly-bagging, labelling, case-building and optimised inbound shipments that avoid Amazon fines.'),
    dict(icon='fa-bullseye', title='PPC &amp; Growth Marketing', text='Sponsored Products/Business campaigns, bid automation, day-parting and creative A/B tests managed to target ACOS/TACoS.'),
    dict(icon='fa-calculator', title='Profit Engineering', text='Landed-cost sheets, fee calculators and pricing rules so every order contributes margin — profitability first, vanity sales never.'),
    dict(icon='fa-handshake', title='Launch &amp; Handover', text='Structured knowledge transfer: SOP manuals, trained operators, dashboards and a 90-day stabilisation plan at handover.')],
  process_sub='Our proven launch-to-handover journey.',
  steps=[
    dict(title='Discovery &amp; Niche Analysis', text='Market sizing, competition mapping and margin modelling on candidate products and lanes (UK/IN).'),
    dict(title='Setup &amp; Sourcing', text='Seller accounts, brand registry, supplier onboarding, QC checklists and first inventory purchase orders.'),
    dict(title='Listings &amp; Store Launch', text='SEO-rich listings, image packs, A+ content, Shopify storefront build and launch calendar executed.'),
    dict(title='Scale &amp; Optimise', text='PPC ramp-up, conversion experiments, inventory forecasting and marketplace event participation (Prime Day, Great Indian Festival).'),
    dict(title='Handover &amp; 24/7 Support', text='Documented SOPs, team training, metric reviews — then ongoing 24/7 operational support to keep profits climbing.')],
  stats=[dict(target=7, desc='Years E-commerce Experience'), dict(target=100, desc='% Projects Handed Over'), dict(target=24, desc='/7 Seller Support'), dict(target=2, desc='Regions Operated (UK &amp; India)')],
  faqs=[
    dict(q='Which marketplaces do you operate on?', a='Primarily Amazon (UK, India and US expansion) and Shopify DTC stores, plus Flipkart and Amazon Brand Registry driven private-label programmes for India-based sellers.'),
    dict(q='What does &ldquo;successful project handover&rdquo; mean?', a='Every engagement ends with a formal handover: documented processes, trained staff or owners, clean account health, KPI dashboard and growth roadmap. Nothing depends on us staying — but most clients keep our 24/7 support anyway.'),
    dict(q='Can you handle UK VAT and India GST for me?', a='Yes. Our compliance desk registers and files UK VAT and Indian GST for marketplace sellers, handles OSS-style reporting where applicable, and keeps your accounts audit-ready.'),
    dict(q='Do you work with existing struggling stores?', a='Frequently. We run a diagnostic on account health, margins and operations, fix the leaks, then either rebuild the engine or hand your team the playbook to run it.'),
    dict(q='How does 24/7 support actually work?', a='Follow-the-sun coverage split between our India and UK teams: order monitoring, buyer messages within prime SLAs, incident response and weekly performance reviews — always a human, always accountable.'),
    dict(q='Will my store be profitable?', a='We engineer profitability before scale — landed-cost discipline, fee-aware pricing and ACOS-targeted ad spend. Our mandate is sustainable profit, and our handover record speaks to it.')],
  cta_text='Launching, scaling or handing over an Amazon/Shopify business? Talk to our 7-year veterans today — free store audit included.'
)
