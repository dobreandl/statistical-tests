package ro.cs.ubbcluj.domain;

import java.util.List;

public class Population implements Entity<Double> {
	private List<Double>features;

	public Population(List<Double> features) {
		super();
		this.features = features;
	}

	@Override
	public List<Double> getFeatureList() {
		return features;
	}
}
