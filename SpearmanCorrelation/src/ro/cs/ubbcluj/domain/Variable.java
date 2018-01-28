package ro.cs.ubbcluj.domain;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import javax.sound.midi.Soundbank;

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

	/**
	 * Determine if a value appears more than once in the list of features, then
	 * we have a tied rank
	 * 
	 * @return true if value will be a tied rank, false otherwise
	 */
	public boolean hasTiedRanks() {
		for (Integer i : features) {
			int frequencies = Collections.frequency(features, i);

			if (frequencies > 1) {
				return true;
			}
		}

		return false;
	}

	/**
	 * Determine the list of positions on which a value appears in the features
	 * list
	 * 
	 * @param value
	 *            from the feature list
	 * @return the list of occurences for value
	 */
	private List<Integer> getFrequencyList(Integer value, List<Integer> list) {
		List<Integer> frequencies = new ArrayList<>();

		for (int i = 0; i < list.size(); i++) {
			Integer val = list.get(i);

			if (val == value) {
				frequencies.add(i + 1);
			}
		}

		return frequencies;
	}

	/**
	 * Compute the mean of a list of integers
	 * 
	 * @param values
	 *            list of integers
	 * @return the mean
	 */
	private Double getMean(List<Integer> values) {
		int sum = 0;
		for (Integer i : values) {
			sum += i;
		}

		return (double) sum / values.size();
	}

	@Override
	public List<Double> computeRanks() {
		List<Double> ranks = new ArrayList<>(Collections.nCopies(features.size(), 0.0));
		List<Integer> sorted = new ArrayList<>(features);
		Collections.sort(sorted, Collections.reverseOrder());

		if (hasTiedRanks()) {

			for (int i = 0; i < features.size(); i++) {
				int pos = features.indexOf(sorted.get(i));
				ranks.set(pos, (double) i + 1);
			}

			for (Integer i : features) {

				List<Integer> frequency = getFrequencyList(i, sorted);

				if (frequency.size() > 1) {
					double mean = getMean(frequency);

					List<Integer> frecqs = getFrequencyList(i, features);

					for(int j=0;j<frecqs.size();j++){
						ranks.set(frecqs.get(j)-1, mean);
					}

				}
			}

		} else {
			for (int i = 0; i < features.size(); i++) {
				int pos = features.indexOf(sorted.get(i));
				ranks.set(pos, (double) i + 1);
			}
		}
		return ranks;
	}

}
