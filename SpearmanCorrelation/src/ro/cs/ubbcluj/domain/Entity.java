package ro.cs.ubbcluj.domain;

import java.util.List;

/**
 * 
 * Generic entity that will be used for Pearson correlation computation
 *
 */
public interface Entity<T> {

	/**
	 * Get the associate list of attributes for the generic entity
	 * @return the list of doubles 
	 */
	public List<T>getFeatureList();
	
	/**
	 * Determine the ranks for the entity based on the list of features
	 * @return list of ranks
	 */
	public List<Double>computeRanks();
	
	/**
	 * Determine if a value appears more than once in the list of features, then
	 * we have a tied rank
	 * 
	 * @return true if value will be a tied rank, false otherwise
	 */
	public boolean hasTiedRanks();
}
