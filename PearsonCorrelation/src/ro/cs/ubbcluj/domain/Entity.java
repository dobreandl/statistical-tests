package ro.cs.ubbcluj.domain;

import java.util.List;

/**
 * 
 * @author SERGIU
 * Generic entity that will be used for Pearson correlation computation
 *
 */
public interface Entity<T> {

	/**
	 * Get the associate list of attributes for the generic entity
	 * @return the list of doubles 
	 */
	public List<T>getFeatureList();
}
