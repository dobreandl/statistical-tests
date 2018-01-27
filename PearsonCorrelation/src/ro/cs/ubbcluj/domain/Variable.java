package ro.cs.ubbcluj.domain;

import java.util.List;

/**
 * 
 * @author SERGIU
 *
 * Concrete entity with a list of doubles
 */
public class Variable implements Entity<Integer> {
	private List<Integer> features;

	public Variable(List<Integer> features) {
		super();
		this.features = features;
	}

	@Override
	public List<Integer> getFeatureList() {
		return features;
	}

}
