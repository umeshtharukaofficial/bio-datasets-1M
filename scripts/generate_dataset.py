#!/usr/bin/env python3
import os
import csv
import random
import datetime
import string
import pandas as pd
import numpy as np
from faker import Faker
from Bio.Seq import Seq

fake = Faker()

CATEGORIES = [
    "genomics",
    "proteomics",
    "ecology",
    "microbiology",
    "botany",
    "zoology",
    "cell-biology",
    "neuroscience",
    "biochemistry",
    "bioinformatics"
]

def generate_short_slug():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=6))

def get_next_id_and_total(manifest_path):
    if not os.path.exists(manifest_path) or os.stat(manifest_path).st_size == 0:
        return 1, 0
    try:
        df = pd.read_csv(manifest_path)
        if df.empty:
            return 1, 0
        max_id = df['id'].max()
        if pd.isna(max_id):
            return 1, 0
        return int(max_id) + 1, len(df)
    except Exception:
        return 1, 0

def generate_data(category, num_rows):
    data = []
    
    # Genomic variables
    dna_bases = ['A', 'C', 'G', 'T']
    genes = ["TP53", "BRCA1", "BRCA2", "EGFR", "MYC", "APOE", "MTHFR", "TNF", "IL6", "VEGFA"]
    
    # Proteomic variables
    amino_acids = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    organisms = ["Homo sapiens", "Mus musculus", "Arabidopsis thaliana", "Saccharomyces cerevisiae", "Escherichia coli", "Drosophila melanogaster", "Caenorhabditis elegans"]
    
    # Ecology variables
    habitats = ["Forest", "Grassland", "Desert", "Tundra", "Marine", "Freshwater", "Wetland", "Urban"]
    
    # Microbiology variables
    colony_types = ["Staphylococcus", "Streptococcus", "Bacillus", "Pseudomonas", "Lactobacillus", "Clostridium"]
    oxygen_requirements = ["Aerobic", "Anaerobic", "Facultative Anaerobe", "Microaerophilic"]
    
    # Botany variables
    botany_families = ["Asteraceae", "Orchidaceae", "Fabaceae", "Poaceae", "Rosaceae", "Brassicaceae", "Solanaceae"]
    flower_colors = ["Red", "Blue", "Yellow", "White", "Pink", "Purple", "Orange", "Green"]
    regions = ["Tropical", "Temperate", "Arid", "Polar", "Mediterranean", "Subtropical"]
    
    # Zoology variables
    zoology_classes = ["Mammalia", "Aves", "Reptilia", "Amphibia", "Actinopterygii"]
    zoology_orders = ["Carnivora", "Rodentia", "Primates", "Passeriformes", "Squamata", "Anura"]
    conservation_statuses = ["Least Concern", "Near Threatened", "Vulnerable", "Endangered", "Critically Endangered", "Extinct in the Wild"]
    
    # Cell Biology variables
    cell_types = ["Stem Cell", "Neuron", "Epithelial", "Myocyte", "Leukocyte", "Erythrocyte", "Fibroblast"]
    
    # Neuroscience variables
    brain_regions = ["Cortex", "Hippocampus", "Cerebellum", "Amygdala", "Thalamus", "Striatum", "Hypothalamus"]
    subject_species_list = ["Mus musculus", "Rattus norvegicus", "Macaca mulatta", "Danio rerio"]
    
    # Biochemistry variables
    compounds = ["Glucose", "Adenosine triphosphate", "Cholesterol", "Aspirin", "Caffeine", "Dopamine", "Serotonin", "Adrenaline", "Ethanol", "Urea"]
    biochem_classes = ["Carbohydrate", "Nucleotide", "Lipid", "Organic Compound", "Alkaloid", "Neurotransmitter", "Hormone", "Alcohol", "Amide"]

    for i in range(num_rows):
        if category == "genomics":
            # sample_id, chromosome, position, ref_allele, alt_allele, gene, quality
            chrom = f"chr{random.randint(1, 22)}" if random.random() < 0.95 else random.choice(["chrX", "chrY"])
            ref = random.choice(dna_bases)
            alt = random.choice([b for b in dna_bases if b != ref])
            data.append({
                "sample_id": f"SMP_{random.randint(1000, 9999)}",
                "chromosome": chrom,
                "position": random.randint(100000, 250000000),
                "ref_allele": ref,
                "alt_allele": alt,
                "gene": random.choice(genes),
                "quality": round(random.uniform(20.0, 99.9), 2)
            })
            
        elif category == "proteomics":
            # protein_id, sequence, length, mass_da, isoelectric_point, organism
            length = random.randint(50, 1500)
            seq = "".join(random.choices(amino_acids, k=length))
            mass = round(length * 110.0 + random.uniform(-500.0, 500.0), 2)
            pi = round(random.uniform(3.0, 12.0), 2)
            data.append({
                "protein_id": f"PRT_{random.randint(10000, 99999)}",
                "sequence": seq,
                "length": length,
                "mass_da": mass,
                "isoelectric_point": pi,
                "organism": random.choice(organisms)
            })
            
        elif category == "ecology":
            # species, latitude, longitude, population, date, habitat
            data.append({
                "species": f"{fake.word().capitalize()} {fake.word()}",
                "latitude": round(random.uniform(-90.0, 90.0), 6),
                "longitude": round(random.uniform(-180.0, 180.0), 6),
                "population": random.randint(10, 100000),
                "date": fake.date_between(start_date='-10y', end_date='today').isoformat(),
                "habitat": random.choice(habitats)
            })
            
        elif category == "microbiology":
            # strain_id, genus, species, gram_stain, oxygen_req, colony_diameter_mm
            genus = random.choice(colony_types)
            data.append({
                "strain_id": f"STR_{random.randint(100, 999)}",
                "genus": genus,
                "species": fake.word(),
                "gram_stain": random.choice(["Positive", "Negative"]),
                "oxygen_req": random.choice(oxygen_requirements),
                "colony_diameter_mm": round(random.uniform(0.5, 10.0), 2)
            })
            
        elif category == "botany":
            # species, family, leaf_length_cm, flower_color, habitat, region
            data.append({
                "species": f"{fake.word().capitalize()} {fake.word()}",
                "family": random.choice(botany_families),
                "leaf_length_cm": round(random.uniform(1.0, 50.0), 2),
                "flower_color": random.choice(flower_colors),
                "habitat": random.choice(habitats),
                "region": random.choice(regions)
            })
            
        elif category == "zoology":
            # species, class, order, weight_kg, length_cm, conservation_status
            data.append({
                "species": f"{fake.word().capitalize()} {fake.word()}",
                "class": random.choice(zoology_classes),
                "order": random.choice(zoology_orders),
                "weight_kg": round(random.uniform(0.005, 5000.0), 3),
                "length_cm": round(random.uniform(1.0, 3000.0), 2),
                "conservation_status": random.choice(conservation_statuses)
            })
            
        elif category == "cell-biology":
            # cell_id, cell_type, diameter_um, organelle_count, viability_pct
            data.append({
                "cell_id": f"CELL_{random.randint(10000, 99999)}",
                "cell_type": random.choice(cell_types),
                "diameter_um": round(random.uniform(5.0, 120.0), 2),
                "organelle_count": random.randint(5, 50),
                "viability_pct": round(random.uniform(50.0, 100.0), 2)
            })
            
        elif category == "neuroscience":
            # neuron_id, region, firing_rate_hz, spike_amplitude_mv, subject_species
            data.append({
                "neuron_id": f"NEUR_{random.randint(1000, 9999)}",
                "region": random.choice(brain_regions),
                "firing_rate_hz": round(random.uniform(0.1, 150.0), 2),
                "spike_amplitude_mv": round(random.uniform(10.0, 120.0), 2),
                "subject_species": random.choice(subject_species_list)
            })
            
        elif category == "biochemistry":
            # compound, formula, mw, pka, solubility_mg_ml, class
            data.append({
                "compound": random.choice(compounds),
                "formula": f"C{random.randint(1,20)}H{random.randint(1,40)}N{random.randint(0,5)}O{random.randint(0,10)}",
                "mw": round(random.uniform(50.0, 1000.0), 2),
                "pka": round(random.uniform(1.0, 14.0), 2) if random.random() > 0.2 else "N/A",
                "solubility_mg_ml": round(random.uniform(0.01, 1000.0), 3),
                "class": random.choice(biochem_classes)
            })
            
        elif category == "bioinformatics":
            # sequence_id, sequence, length, gc_content, source_organism
            length = random.randint(50, 2000)
            seq = "".join(random.choices(dna_bases, k=length))
            gc = round((seq.count('G') + seq.count('C')) / length * 100, 2)
            data.append({
                "sequence_id": f"SEQ_{random.randint(100000, 999999)}",
                "sequence": seq,
                "length": length,
                "gc_content": gc,
                "source_organism": random.choice(organisms)
            })

    return pd.DataFrame(data)

def main():
    manifest_path = "manifest/index.csv"
    
    # Read stats
    next_id, current_total = get_next_id_and_total(manifest_path)
    
    # Check stop condition
    if current_total >= 1_000_000:
        print("Target of 1,000,000 datasets reached. Stopping.")
        return
        
    category = random.choice(CATEGORIES)
    num_rows = random.randint(100, 5000)
    slug = generate_short_slug()
    
    filename = f"{category}_{next_id}_{slug}.csv"
    filepath = os.path.join("datasets", category, filename)
    
    # Generate data
    df = generate_data(category, num_rows)
    
    # Write dataset to disk
    df.to_csv(filepath, index=False)
    print(f"Generated dataset {filename} in datasets/{category}/ with {num_rows} rows.")
    
    # Log to manifest/index.csv
    created_at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Write using standard CSV writer to avoid formatting issues
    with open(manifest_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([next_id, category, filename, num_rows, created_at])

if __name__ == "__main__":
    main()
